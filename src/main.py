from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.db.connection import connectDb, closeDb
from src.api import orgRoutes, adminRoutes

# Create FastAPI app
app = FastAPI(
    title="Organization Management Service",
    description="Backend service for managing organizations with dynamic collections",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Startup event
@app.on_event("startup")
async def startup():
    """Initialize database connection on startup"""
    await connectDb()
    print("✓ Application started successfully")

# Shutdown event
@app.on_event("shutdown")
async def shutdown():
    """Close database connection on shutdown"""
    await closeDb()
    print("✓ Application shutdown complete")

# Root route
@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "working"}

# Include routers
app.include_router(orgRoutes.router)
app.include_router(adminRoutes.router)

# Run with: uvicorn src.main:app --reload
