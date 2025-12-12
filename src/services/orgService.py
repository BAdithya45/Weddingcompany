import re
from src.db.masterRepo import MasterRepo
from src.db.dynamicRepo import DynamicRepo
from src.utils.hashService import HashService

class OrgService:
    """Business logic for organization operations"""
    
    def __init__(self):
        self.masterRepo = MasterRepo()
        self.dynamicRepo = DynamicRepo()
        self.hashService = HashService()
    
    def generateCollectionName(self, organizationName: str) -> str:
        """Generate camelCase collection name from organization name"""
        # Remove special characters and spaces
        cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', organizationName)
        # Split into words
        words = cleaned.split()
        if not words:
            raise ValueError("Invalid organization name")
        
        # Create camelCase: first word lowercase, rest capitalized
        collectionName = words[0].lower()
        for word in words[1:]:
            collectionName += word.capitalize()
        
        # Prefix with 'org'
        return f"org{collectionName.capitalize()}"
    
    async def createOrganization(self, organizationName: str, email: str, password: str):
        """Create new organization with admin user"""
        # Check if organization already exists
        existing = await self.masterRepo.findByName(organizationName)
        if existing:
            raise Exception("Organization name already exists")
        
        # Check if email is already used
        existingEmail = await self.masterRepo.findByEmail(email)
        if existingEmail:
            raise Exception("Email already registered")
        
        # Generate collection name
        collectionName = self.generateCollectionName(organizationName)
        
        # Hash password
        hashedPassword = self.hashService.hashPassword(password)
        
        # Create organization metadata
        orgData = {
            "organizationName": organizationName,
            "dynamicCollectionName": collectionName,
            "email": email,
            "password": hashedPassword
        }
        
        # Save to master database
        orgId = await self.masterRepo.createOrg(orgData)
        
        # Create dynamic collection
        await self.dynamicRepo.createCollection(collectionName)
        
        return {
            "success": True,
            "message": "Organization created successfully",
            "organizationId": orgId,
            "organizationName": organizationName,
            "collectionName": collectionName
        }
    
    async def getOrganization(self, organizationName: str):
        """Get organization details"""
        org = await self.masterRepo.findByName(organizationName)
        if not org:
            raise Exception("Organization not found")
        
        # Remove sensitive data
        org.pop("password", None)
        org["_id"] = str(org["_id"])
        
        return {
            "success": True,
            "organization": org
        }
    
    async def updateOrganization(self, oldName: str, newName: str, email: str, password: str):
        """Update organization name and details"""
        # Find existing organization
        org = await self.masterRepo.findByName(oldName)
        if not org:
            raise Exception("Organization not found")
        
        # If name is changing, check new name availability
        if oldName != newName:
            existing = await self.masterRepo.findByName(newName)
            if existing:
                raise Exception("New organization name already exists")
        
        # Generate new collection name
        newCollectionName = self.generateCollectionName(newName)
        oldCollectionName = org["dynamicCollectionName"]
        
        # Hash new password
        hashedPassword = self.hashService.hashPassword(password)
        
        # If collection name changes, migrate data
        if oldCollectionName != newCollectionName:
            # Copy data to new collection
            await self.dynamicRepo.copyData(oldCollectionName, newCollectionName)
            # Drop old collection
            await self.dynamicRepo.dropCollection(oldCollectionName)
        
        # Update master database
        updateData = {
            "organizationName": newName,
            "dynamicCollectionName": newCollectionName,
            "email": email,
            "password": hashedPassword
        }
        
        await self.masterRepo.updateOrg(oldName, updateData)
        
        return {
            "success": True,
            "message": "Organization updated successfully",
            "organizationName": newName,
            "collectionName": newCollectionName
        }
    
    async def deleteOrganization(self, organizationName: str):
        """Delete organization and its data"""
        # Find organization
        org = await self.masterRepo.findByName(organizationName)
        if not org:
            raise Exception("Organization not found")
        
        collectionName = org["dynamicCollectionName"]
        
        # Drop dynamic collection
        await self.dynamicRepo.dropCollection(collectionName)
        
        # Delete from master database
        await self.masterRepo.deleteOrg(organizationName)
        
        return {
            "success": True,
            "message": "Organization deleted successfully"
        }
