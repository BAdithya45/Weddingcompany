import bcrypt

class HashService:
    """Service for password hashing and verification"""
    
    @staticmethod
    def hashPassword(password: str) -> str:
        """Hash a plain text password"""
        passwordBytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashedPassword = bcrypt.hashpw(passwordBytes, salt)
        return hashedPassword.decode('utf-8')
    
    @staticmethod
    def verifyPassword(plainPassword: str, hashedPassword: str) -> bool:
        """Verify a password against its hash"""
        passwordBytes = plainPassword.encode('utf-8')
        hashedBytes = hashedPassword.encode('utf-8')
        return bcrypt.checkpw(passwordBytes, hashedBytes)
