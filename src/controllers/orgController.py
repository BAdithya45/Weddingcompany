from pydantic import BaseModel, EmailStr
from src.services.orgService import OrgService

class CreateOrgRequest(BaseModel):
    organizationName: str
    email: EmailStr
    password: str

class GetOrgRequest(BaseModel):
    organizationName: str

class UpdateOrgRequest(BaseModel):
    organizationName: str
    newOrganizationName: str
    email: EmailStr
    password: str

class DeleteOrgRequest(BaseModel):
    organizationName: str

class OrgController:
    """Controller for organization endpoints"""
    
    def __init__(self):
        self.orgService = OrgService()
    
    async def createOrg(self, request: CreateOrgRequest):
        """Handle create organization request"""
        try:
            result = await self.orgService.createOrganization(
                request.organizationName,
                request.email,
                request.password
            )
            return result
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    async def getOrg(self, organizationName: str):
        """Handle get organization request"""
        try:
            result = await self.orgService.getOrganization(organizationName)
            return result
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    async def updateOrg(self, request: UpdateOrgRequest):
        """Handle update organization request"""
        try:
            result = await self.orgService.updateOrganization(
                request.organizationName,
                request.newOrganizationName,
                request.email,
                request.password
            )
            return result
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    async def deleteOrg(self, organizationName: str):
        """Handle delete organization request"""
        try:
            result = await self.orgService.deleteOrganization(organizationName)
            return result
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
