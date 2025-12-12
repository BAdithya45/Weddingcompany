from fastapi import APIRouter, Header, HTTPException
from typing import Optional
from src.controllers.orgController import (
    OrgController,
    CreateOrgRequest,
    UpdateOrgRequest,
    DeleteOrgRequest
)
from src.controllers.adminController import AdminController

router = APIRouter(prefix="/org", tags=["Organization"])
orgController = OrgController()
adminController = AdminController()

async def verifyAuth(authorization: Optional[str] = Header(None)):
    """Verify JWT token for protected routes"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header required")
    
    result = await adminController.verifyToken(authorization)
    if not result.get("success"):
        raise HTTPException(status_code=401, detail=result.get("error"))
    
    return result

@router.post("/create")
async def createOrg(request: CreateOrgRequest):
    """Create new organization"""
    result = await orgController.createOrg(request)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("error"))
    return result

@router.get("/get")
async def getOrg(organizationName: str):
    """Get organization details"""
    result = await orgController.getOrg(organizationName)
    if not result.get("success"):
        raise HTTPException(status_code=404, detail=result.get("error"))
    return result

@router.put("/update")
async def updateOrg(request: UpdateOrgRequest, authorization: Optional[str] = Header(None)):
    """Update organization (protected route)"""
    # Verify authentication
    auth = await verifyAuth(authorization)
    
    # Check if user owns this organization
    if auth["organizationName"] != request.organizationName:
        raise HTTPException(status_code=403, detail="Not authorized to update this organization")
    
    result = await orgController.updateOrg(request)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("error"))
    return result

@router.delete("/delete")
async def deleteOrg(organizationName: str, authorization: Optional[str] = Header(None)):
    """Delete organization (protected route)"""
    # Verify authentication
    auth = await verifyAuth(authorization)
    
    # Check if user owns this organization
    if auth["organizationName"] != organizationName:
        raise HTTPException(status_code=403, detail="Not authorized to delete this organization")
    
    result = await orgController.deleteOrg(organizationName)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("error"))
    return result
