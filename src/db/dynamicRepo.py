from src.db.connection import getDb

class DynamicRepo:
    """Repository for dynamic organization collections"""
    
    async def createCollection(self, collectionName: str):
        """Create a new dynamic collection"""
        db = getDb()
        # MongoDB creates collections automatically on first insert
        # We'll just verify it exists by creating an empty structure
        collection = db[collectionName]
        return collection
    
    async def getCollection(self, collectionName: str):
        """Get reference to dynamic collection"""
        db = getDb()
        return db[collectionName]
    
    async def copyData(self, sourceCollection: str, targetCollection: str):
        """Copy all data from source to target collection"""
        db = getDb()
        source = db[sourceCollection]
        target = db[targetCollection]
        
        # Get all documents from source
        documents = await source.find().to_list(length=None)
        
        if documents:
            # Remove _id to let MongoDB generate new ones
            for doc in documents:
                doc.pop("_id", None)
            await target.insert_many(documents)
        
        return len(documents)
    
    async def dropCollection(self, collectionName: str):
        """Delete a dynamic collection"""
        db = getDb()
        await db[collectionName].drop()
        return True
    
    async def collectionExists(self, collectionName: str):
        """Check if collection exists"""
        db = getDb()
        collections = await db.list_collection_names()
        return collectionName in collections
