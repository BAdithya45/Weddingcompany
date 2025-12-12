from fastapi import APIRouter, HTTPException
from src.controllers.adminController import AdminController, LoginRequest

router = APIRouter(prefix="/admin", tags=["Admin"])
adminController = AdminController()

@router.post("/login")
async def login(request: LoginRequest):
    """Admin login endpoint"""
    result = await adminController.login(request)
    if not result.get("success"):
        raise HTTPException(status_code=401, detail=result.get("error"))
    return result
