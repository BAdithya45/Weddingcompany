import os
import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

class TokenService:
    """Service for JWT token generation and validation"""
    
    def __init__(self):
        self.secret = os.getenv("JWT_SECRET", "default-secret-key")
        self.algorithm = os.getenv("JWT_ALGORITHM", "HS256")
        self.expireHours = int(os.getenv("JWT_EXPIRE_HOURS", "24"))
    
    def createToken(self, adminId: str, organizationName: str) -> str:
        """Generate JWT token for authenticated admin"""
        payload = {
            "adminId": adminId,
            "organizationName": organizationName,
            "exp": datetime.utcnow() + timedelta(hours=self.expireHours),
            "iat": datetime.utcnow()
        }
        token = jwt.encode(payload, self.secret, algorithm=self.algorithm)
        return token
    
    def verifyToken(self, token: str) -> dict:
        """Verify and decode JWT token"""
        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")
    
    def extractToken(self, authHeader: str) -> str:
        """Extract token from Authorization header"""
        if not authHeader:
            raise Exception("Authorization header missing")
        
        parts = authHeader.split()
        if len(parts) != 2 or parts[0].lower() != "bearer":
            raise Exception("Invalid authorization header format")
        
        return parts[1]
