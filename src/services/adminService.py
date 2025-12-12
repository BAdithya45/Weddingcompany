from src.db.masterRepo import MasterRepo
from src.utils.hashService import HashService
from src.utils.tokenService import TokenService

class AdminService:
    """Business logic for admin authentication"""
    
    def __init__(self):
        self.masterRepo = MasterRepo()
        self.hashService = HashService()
        self.tokenService = TokenService()
    
    async def loginAdmin(self, email: str, password: str):
        """Authenticate admin and return JWT token"""
        # Find organization by email
        org = await self.masterRepo.findByEmail(email)
        if not org:
            raise Exception("Invalid email or password")
        
        # Verify password
        isValid = self.hashService.verifyPassword(password, org["password"])
        if not isValid:
            raise Exception("Invalid email or password")
        
        # Generate JWT token
        adminId = str(org["_id"])
        organizationName = org["organizationName"]
        token = self.tokenService.createToken(adminId, organizationName)
        
        return {
            "success": True,
            "message": "Login successful",
            "token": token,
            "adminId": adminId,
            "organizationName": organizationName
        }
    
    async def verifyAdmin(self, token: str):
        """Verify admin token"""
        try:
            payload = self.tokenService.verifyToken(token)
            return {
                "success": True,
                "adminId": payload["adminId"],
                "organizationName": payload["organizationName"]
            }
        except Exception as e:
            raise Exception(f"Authentication failed: {str(e)}")
