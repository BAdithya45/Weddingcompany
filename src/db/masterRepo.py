from datetime import datetime
from src.db.connection import getDb

class MasterRepo:
    """Repository for master database operations"""
    
    def __init__(self):
        self.collectionName = "organizations"
    
    async def findByName(self, organizationName: str):
        """Find organization by name"""
        db = getDb()
        collection = db[self.collectionName]
        return await collection.find_one({"organizationName": organizationName})
    
    async def findByEmail(self, email: str):
        """Find organization by admin email"""
        db = getDb()
        collection = db[self.collectionName]
        return await collection.find_one({"email": email})
    
    async def createOrg(self, orgData: dict):
        """Create new organization in master database"""
        db = getDb()
        collection = db[self.collectionName]
        orgData["createdAt"] = datetime.utcnow()
        orgData["updatedAt"] = datetime.utcnow()
        result = await collection.insert_one(orgData)
        return str(result.inserted_id)
    
    async def updateOrg(self, oldName: str, newData: dict):
        """Update organization metadata"""
        db = getDb()
        collection = db[self.collectionName]
        newData["updatedAt"] = datetime.utcnow()
        result = await collection.update_one(
            {"organizationName": oldName},
            {"$set": newData}
        )
        return result.modified_count > 0
    
    async def deleteOrg(self, organizationName: str):
        """Delete organization from master database"""
        db = getDb()
        collection = db[self.collectionName]
        result = await collection.delete_one({"organizationName": organizationName})
        return result.deleted_count > 0
