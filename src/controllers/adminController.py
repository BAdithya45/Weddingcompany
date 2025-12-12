from pydantic import BaseModel, EmailStr
from src.services.adminService import AdminService

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class AdminController:
    """Controller for admin endpoints"""
    
    def __init__(self):
        self.adminService = AdminService()
    
    async def login(self, request: LoginRequest):
        """Handle admin login request"""
        try:
            result = await self.adminService.loginAdmin(
                request.email,
                request.password
            )
            return result
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    async def verifyToken(self, authHeader: str):
        """Verify JWT token from header"""
        try:
            from src.utils.tokenService import TokenService
            tokenService = TokenService()
            token = tokenService.extractToken(authHeader)
            result = await self.adminService.verifyAdmin(token)
            return result
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
