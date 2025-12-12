# Deployment Guide - Organization Management Service

## 🚀 Quick Deployment Options

This guide covers deploying your FastAPI backend to Render or Railway.

---

## Option 1: Deploy to Render (Recommended)

### Step 1: Prepare MongoDB Atlas

1. Create account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a free cluster
3. Add database user with password
4. Whitelist all IPs (0.0.0.0/0) for Render
5. Get connection string: `mongodb+srv://username:password@cluster.mongodb.net/`

### Step 2: Push to GitHub

```bash
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

### Step 3: Deploy on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub account
4. Select your repository
5. Configure:
   - **Name:** organization-management-api
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn src.main:app --host 0.0.0.0 --port $PORT`
   - **Plan:** Free

6. Add Environment Variables:
   ```
   MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/
   DATABASE_NAME=organizationMaster
   JWT_SECRET=your-super-secret-production-key-min-32-chars
   JWT_ALGORITHM=HS256
   JWT_EXPIRE_HOURS=24
   ```

7. Click **"Create Web Service"**

8. Wait for deployment (5-10 minutes)

9. Your API will be live at:
   ```
   https://your-service-name.onrender.com
   ```

### Step 4: Test Deployment

```bash
curl https://your-service-name.onrender.com/
```

Expected response:
```json
{"status": "working"}
```

---

## Option 2: Deploy to Railway

### Step 1: Prepare MongoDB (same as above)

### Step 2: Push to GitHub (same as above)

### Step 3: Deploy on Railway

1. Go to [Railway](https://railway.app/)
2. Sign in with GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Select your repository
5. Railway auto-detects Python and builds

6. Add Environment Variables:
   - Click on your service
   - Go to **"Variables"** tab
   - Add:
     ```
     MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/
     DATABASE_NAME=organizationMaster
     JWT_SECRET=your-super-secret-production-key-min-32-chars
     JWT_ALGORITHM=HS256
     JWT_EXPIRE_HOURS=24
     ```

7. Generate domain:
   - Go to **"Settings"**
   - Click **"Generate Domain"**

8. Your API will be live at:
   ```
   https://your-project.railway.app
   ```

---

## 🧪 Testing Your Deployed API

### 1. Health Check
```bash
curl https://your-api-url.com/
```

### 2. Create Organization
```bash
curl -X POST https://your-api-url.com/org/create \
  -H "Content-Type: application/json" \
  -d '{
    "organizationName": "Test Company",
    "email": "admin@test.com",
    "password": "test123456"
  }'
```

### 3. Login
```bash
curl -X POST https://your-api-url.com/admin/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@test.com",
    "password": "test123456"
  }'
```

Save the token from response!

### 4. Get Organization
```bash
curl https://your-api-url.com/org/get?organizationName=Test%20Company
```

### 5. Update Organization (with auth)
```bash
curl -X PUT https://your-api-url.com/org/update \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "organizationName": "Test Company",
    "newOrganizationName": "Test Industries",
    "email": "admin@testindustries.com",
    "password": "newpass123"
  }'
```

### 6. Delete Organization (with auth)
```bash
curl -X DELETE "https://your-api-url.com/org/delete?organizationName=Test%20Industries" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

---

## 📊 View API Documentation

Once deployed, visit:
```
https://your-api-url.com/docs
```

This opens FastAPI's interactive Swagger UI where you can:
- See all endpoints
- Test API calls directly
- View request/response schemas

---

## 🔧 Troubleshooting

### Issue: MongoDB Connection Failed
- Check MongoDB Atlas IP whitelist (should include 0.0.0.0/0)
- Verify connection string is correct
- Check database user permissions

### Issue: 502 Bad Gateway on Render
- Check build logs for errors
- Verify start command is correct
- Ensure all dependencies in requirements.txt

### Issue: Module Not Found
- Check Python version compatibility
- Verify requirements.txt includes all packages
- Clear build cache and redeploy

### Issue: JWT Token Errors
- Ensure JWT_SECRET is set in environment variables
- Check token expiry time
- Verify Authorization header format: `Bearer <token>`

---

## 🔒 Production Checklist

- ✅ MongoDB Atlas cluster created
- ✅ Strong JWT_SECRET (min 32 characters)
- ✅ Environment variables set correctly
- ✅ Code pushed to GitHub
- ✅ Service deployed and running
- ✅ Health check returns `{"status": "working"}`
- ✅ All API endpoints tested
- ✅ CORS configured for your frontend domain
- ✅ MongoDB IP whitelist configured
- ✅ Logs monitored for errors

---

## 📈 Monitoring Your Deployment

### Render
- View logs: Dashboard → Your Service → Logs
- Check metrics: Dashboard → Your Service → Metrics

### Railway
- View logs: Project → Service → Deployments → View Logs
- Check metrics: Project → Service → Metrics

---

## 🎉 Success!

Your Organization Management Service is now deployed and accessible publicly!

Share your API URL:
```
https://your-service-name.onrender.com
```

or

```
https://your-project.railway.app
```

---

## 📞 Need Help?

- Check logs first
- Review environment variables
- Test locally before deploying
- Open GitHub issue for support
