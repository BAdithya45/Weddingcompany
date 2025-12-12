# Organization Management Service

A FastAPI-based backend service for managing organizations with dynamic MongoDB collections and JWT authentication.

## 🎯 Features

- Create organizations with dynamic MongoDB collections
- Admin authentication with JWT tokens
- Update organization details with automatic data migration
- Delete organizations securely
- Password hashing with bcrypt
- RESTful API design
- Fully deployable on Render or Railway

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    FastAPI Application                   │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────┐         ┌──────────────┐             │
│  │   Org Routes │         │ Admin Routes │             │
│  └──────┬───────┘         └──────┬───────┘             │
│         │                        │                      │
│  ┌──────▼───────┐         ┌──────▼───────┐             │
│  │Org Controller│         │Admin Control │             │
│  └──────┬───────┘         └──────┬───────┘             │
│         │                        │                      │
│  ┌──────▼───────┐         ┌──────▼───────┐             │
│  │ Org Service  │         │Admin Service │             │
│  └──────┬───────┘         └──────┬───────┘             │
│         │                        │                      │
│  ┌──────▼──────────────────────▼─────────┐             │
│  │         Utility Services              │             │
│  │  - Hash Service (bcrypt)              │             │
│  │  - Token Service (JWT)                │             │
│  └───────────────────────────────────────┘             │
│                                                          │
│  ┌──────────────────────────────────────┐              │
│  │      Database Repositories           │              │
│  │  - Master Repo (organizations)       │              │
│  │  - Dynamic Repo (org collections)    │              │
│  └──────────────┬───────────────────────┘              │
│                 │                                       │
└─────────────────┼───────────────────────────────────────┘
                  │
        ┌─────────▼──────────┐
        │   MongoDB Atlas    │
        │                    │
        │  - Master DB       │
        │  - Dynamic Colls   │
        └────────────────────┘
```

## 📁 Project Structure

```
src/
├── main.py                    # FastAPI app entry point
├── api/
│   ├── orgRoutes.py          # Organization endpoints
│   └── adminRoutes.py        # Admin authentication endpoints
├── controllers/
│   ├── orgController.py      # Organization request handlers
│   └── adminController.py    # Admin request handlers
├── services/
│   ├── orgService.py         # Organization business logic
│   └── adminService.py       # Admin business logic
├── db/
│   ├── connection.py         # MongoDB connection
│   ├── masterRepo.py         # Master database operations
│   └── dynamicRepo.py        # Dynamic collection operations
└── utils/
    ├── hashService.py        # Password hashing
    └── tokenService.py       # JWT token management
```

## 🚀 Local Setup

### Prerequisites

- Python 3.8+
- MongoDB (local or Atlas)
- Git

### Installation Steps

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd wedding
```

2. **Create virtual environment**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
cp .env.example .env
```

Edit `.env` file with your settings:
```
MONGO_URL=mongodb://localhost:27017
DATABASE_NAME=organizationMaster
JWT_SECRET=your-secret-key-here
JWT_ALGORITHM=HS256
JWT_EXPIRE_HOURS=24
```

5. **Run the application**
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

## 📡 API Endpoints

### Root
- **GET** `/` - Health check
  ```bash
  curl http://localhost:8000/
  ```
  Response: `{"status": "working"}`

### Organization Management

#### 1. Create Organization
- **POST** `/org/create`
- **Body:**
  ```json
  {
    "organizationName": "Tech Corp",
    "email": "admin@techcorp.com",
    "password": "securePassword123"
  }
  ```
- **Example:**
  ```bash
  curl -X POST http://localhost:8000/org/create \
    -H "Content-Type: application/json" \
    -d '{
      "organizationName": "Tech Corp",
      "email": "admin@techcorp.com",
      "password": "securePassword123"
    }'
  ```

#### 2. Get Organization
- **GET** `/org/get?organizationName=Tech Corp`
- **Example:**
  ```bash
  curl http://localhost:8000/org/get?organizationName=Tech%20Corp
  ```

#### 3. Update Organization
- **PUT** `/org/update`
- **Headers:** `Authorization: Bearer <token>`
- **Body:**
  ```json
  {
    "organizationName": "Tech Corp",
    "newOrganizationName": "Tech Industries",
    "email": "admin@techindustries.com",
    "password": "newPassword123"
  }
  ```
- **Example:**
  ```bash
  curl -X PUT http://localhost:8000/org/update \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <your-token>" \
    -d '{
      "organizationName": "Tech Corp",
      "newOrganizationName": "Tech Industries",
      "email": "admin@techindustries.com",
      "password": "newPassword123"
    }'
  ```

#### 4. Delete Organization
- **DELETE** `/org/delete?organizationName=Tech Corp`
- **Headers:** `Authorization: Bearer <token>`
- **Example:**
  ```bash
  curl -X DELETE "http://localhost:8000/org/delete?organizationName=Tech%20Corp" \
    -H "Authorization: Bearer <your-token>"
  ```

### Admin Authentication

#### Login
- **POST** `/admin/login`
- **Body:**
  ```json
  {
    "email": "admin@techcorp.com",
    "password": "securePassword123"
  }
  ```
- **Example:**
  ```bash
  curl -X POST http://localhost:8000/admin/login \
    -H "Content-Type: application/json" \
    -d '{
      "email": "admin@techcorp.com",
      "password": "securePassword123"
    }'
  ```

## 🌐 Deployment

### Deploy to Render

1. **Push code to GitHub**
```bash
git add .
git commit -m "ready for deployment"
git push origin main
```

2. **Create Render account** at https://render.com

3. **Create new Web Service**
   - Connect your GitHub repository
   - Select the `wedding` repository
   - Configure:
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `uvicorn src.main:app --host 0.0.0.0 --port $PORT`

4. **Add environment variables** in Render dashboard:
   ```
   MONGO_URL=mongodb+srv://user:pass@cluster.mongodb.net/
   DATABASE_NAME=organizationMaster
   JWT_SECRET=your-production-secret
   JWT_ALGORITHM=HS256
   JWT_EXPIRE_HOURS=24
   ```

5. **Deploy** and get your public URL

### Deploy to Railway

1. **Push code to GitHub**

2. **Create Railway account** at https://railway.app

3. **Create new project**
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway auto-detects Python

4. **Add environment variables**

5. **Deploy** and get your public URL

## 🔒 Security Considerations

- Passwords are hashed using bcrypt
- JWT tokens expire after 24 hours (configurable)
- Protected routes require valid JWT token
- Admin can only modify their own organization
- MongoDB connection uses environment variables

## 📊 Database Schema

### Master Database Collection: `organizations`
```javascript
{
  "_id": ObjectId,
  "organizationName": "Tech Corp",
  "dynamicCollectionName": "orgTechcorp",
  "email": "admin@techcorp.com",
  "password": "$2b$12$hashed...",
  "createdAt": ISODate,
  "updatedAt": ISODate
}
```

### Dynamic Collections
Each organization gets a collection named `org{OrganizationName}` in camelCase.
Can store any organization-specific data.

## 🎯 Design Decisions & Tradeoffs

### Dynamic Collections
**Pros:**
- Data isolation per organization
- Flexible schema per organization
- Easy to scale horizontally

**Cons:**
- More complex to query across organizations
- Collection management overhead

### JWT Authentication
**Pros:**
- Stateless authentication
- Scalable
- Works across services

**Cons:**
- Cannot revoke tokens before expiry
- Token size can grow with claims

### camelCase Naming
Following your requirements, all variables use camelCase without underscores for clean, readable code.

## 🧪 Testing the API

Use the included curl commands or import into Postman:

1. Create an organization
2. Login to get JWT token
3. Use token to update/delete organization
4. Verify all operations work correctly

## 📝 Notes

- All variable names use camelCase (no underscores)
- Clean, human-readable code
- Regular git commits for tracking
- Production-ready with proper error handling
- Scalable architecture

## 🤝 Support

For issues or questions, please open a GitHub issue.

## 📄 License

MIT License - feel free to use for your projects!
