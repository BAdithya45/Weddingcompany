import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

# MongoDB connection settings
mongoUrl = os.getenv("MONGO_URL", "mongodb://localhost:27017")
databaseName = os.getenv("DATABASE_NAME", "organizationMaster")

# Global client instance
client = None
database = None

async def connectDb():
    """Connect to MongoDB database"""
    global client, database
    try:
        client = AsyncIOMotorClient(mongoUrl, serverSelectionTimeoutMS=5000)
        database = client[databaseName]
        # Test connection
        await client.admin.command('ping')
        print(f"✓ Connected to MongoDB: {databaseName}")
        return database
    except Exception as e:
        print(f"✗ Failed to connect to MongoDB: {str(e)}")
        raise

async def closeDb():
    """Close MongoDB connection"""
    global client
    if client:
        client.close()
        print("✓ MongoDB connection closed")

def getDb():
    """Get database instance"""
    return database
