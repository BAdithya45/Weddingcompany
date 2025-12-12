# ⚡ Quick Start Guide

Get the Organization Management Service running in 5 minutes!

---

## 🚀 Fast Track Setup

### 1️⃣ Clone and Install (2 minutes)

```bash
# Navigate to project
cd "c:\Users\Adithya Bhaskar\Desktop\Projects\wedding"

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Setup MongoDB (1 minute)

**Option A: MongoDB Atlas (Recommended for deployment)**
1. Go to https://www.mongodb.com/cloud/atlas
2. Create free cluster
3. Get connection string
4. Update `.env` file

**Option B: Local MongoDB (For testing)**
1. Install MongoDB locally
2. Start MongoDB service
3. Use: `mongodb://localhost:27017`

### 3️⃣ Configure Environment (.env already created!)

The `.env` file is ready. Just update if using MongoDB Atlas:
```
MONGO_URL=mongodb+srv://user:pass@cluster.mongodb.net/
DATABASE_NAME=organizationMaster
JWT_SECRET=super-secret-key-change-this-in-production
```

### 4️⃣ Run Server (30 seconds)

```bash
uvicorn src.main:app --reload
```

**Server running at:** `http://localhost:8000` ✅

### 5️⃣ Test It! (1 minute)

**Open browser:**
```
http://localhost:8000/docs
```

**Or use curl:**
```bash
# Health check
curl http://localhost:8000/

# Create organization
curl -X POST http://localhost:8000/org/create \
  -H "Content-Type: application/json" \
  -d '{
    "organizationName": "Quick Test",
    "email": "test@example.com",
    "password": "test123456"
  }'
```

---

## 🌐 Deploy to Production (5 minutes)

### Option 1: Render

```bash
# 1. Push to GitHub
git remote add origin https://github.com/yourusername/org-management.git
git push -u origin main

# 2. Go to Render.com
# 3. Connect GitHub repo
# 4. Add MONGO_URL variable
# 5. Deploy!
```

**Done! Get your URL:** `https://your-service.onrender.com`

### Option 2: Railway

```bash
# 1. Push to GitHub (same as above)

# 2. Go to Railway.app
# 3. Deploy from GitHub
# 4. Add environment variables
# 5. Generate domain
```

**Done! Get your URL:** `https://your-project.railway.app`

---

## 📱 Test Your Deployed API

```bash
# Replace with your actual URL
export API_URL=https://your-service.onrender.com

# Test health
curl $API_URL/

# Create org
curl -X POST $API_URL/org/create \
  -H "Content-Type: application/json" \
  -d '{
    "organizationName": "Live Test",
    "email": "admin@livetest.com",
    "password": "secure123"
  }'

# Login
curl -X POST $API_URL/admin/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@livetest.com",
    "password": "secure123"
  }'
```

---

## 📚 Full Documentation

- **README.md** - Complete project documentation
- **DEPLOYMENT.md** - Detailed deployment guide  
- **API_TESTING.md** - All API test commands
- **PROJECT_SUMMARY.md** - Project completion checklist

---

## 🎯 All Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/` | No | Health check |
| POST | `/org/create` | No | Create organization |
| GET | `/org/get` | No | Get organization |
| PUT | `/org/update` | Yes | Update organization |
| DELETE | `/org/delete` | Yes | Delete organization |
| POST | `/admin/login` | No | Admin login |

---

## 🛠️ Troubleshooting

### Server won't start?
```bash
# Check Python version (need 3.8+)
python --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Can't connect to MongoDB?
```bash
# Check MongoDB is running (if local)
# Or verify Atlas connection string in .env
```

### Import errors?
```bash
# Make sure you're in project root
# Activate virtual environment
venv\Scripts\activate
```

---

## ✅ Success Indicators

You'll know everything works when:
- ✅ Server starts without errors
- ✅ `/` returns `{"status": "working"}`
- ✅ Can create organization
- ✅ Can login and get token
- ✅ Interactive docs work at `/docs`

---

## 🎉 You're Ready!

Your Organization Management Service is:
- 🚀 Running locally
- 📡 API endpoints working
- 🔒 Authentication enabled
- 📝 Fully documented
- ☁️ Ready to deploy

**Next:** Push to GitHub → Deploy to Render/Railway → Share your public URL!

---

## 💡 Quick Tips

1. **Use `/docs`** for interactive testing (super easy!)
2. **Save JWT tokens** after login for protected routes
3. **Test locally first** before deploying
4. **Check logs** if something goes wrong
5. **Read error messages** - they're helpful!

---

## 🆘 Need Help?

1. Check the error message
2. Look at server logs
3. Review README.md
4. Check DEPLOYMENT.md
5. Verify environment variables

---

**Happy Coding! 🎊**

*This is production-ready code. Deploy with confidence!*
