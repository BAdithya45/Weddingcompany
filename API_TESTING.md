# API Testing Collection

Complete set of curl commands to test all API endpoints.

## Setup

Replace `BASE_URL` with your deployment URL:
- Local: `http://localhost:8000`
- Render: `https://your-service.onrender.com`
- Railway: `https://your-project.railway.app`

```bash
export BASE_URL=http://localhost:8000
```

---

## 1. Health Check

```bash
curl $BASE_URL/
```

**Expected Response:**
```json
{"status": "working"}
```

---

## 2. Create Organization

```bash
curl -X POST $BASE_URL/org/create \
  -H "Content-Type: application/json" \
  -d '{
    "organizationName": "Tech Innovations",
    "email": "admin@techinnovations.com",
    "password": "SecurePass123!"
  }'
```

**Expected Response:**
```json
{
  "success": true,
  "message": "Organization created successfully",
  "organizationId": "507f1f77bcf86cd799439011",
  "organizationName": "Tech Innovations",
  "collectionName": "orgTechinnovations"
}
```

---

## 3. Admin Login

```bash
curl -X POST $BASE_URL/admin/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@techinnovations.com",
    "password": "SecurePass123!"
  }'
```

**Expected Response:**
```json
{
  "success": true,
  "message": "Login successful",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "adminId": "507f1f77bcf86cd799439011",
  "organizationName": "Tech Innovations"
}
```

**Save the token:**
```bash
export TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

## 4. Get Organization

```bash
curl "$BASE_URL/org/get?organizationName=Tech%20Innovations"
```

**Expected Response:**
```json
{
  "success": true,
  "organization": {
    "_id": "507f1f77bcf86cd799439011",
    "organizationName": "Tech Innovations",
    "dynamicCollectionName": "orgTechinnovations",
    "email": "admin@techinnovations.com",
    "createdAt": "2025-12-12T10:30:00.000Z",
    "updatedAt": "2025-12-12T10:30:00.000Z"
  }
}
```

---

## 5. Update Organization

**Requires Authentication!**

```bash
curl -X PUT $BASE_URL/org/update \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "organizationName": "Tech Innovations",
    "newOrganizationName": "Tech Solutions Global",
    "email": "admin@techsolutions.com",
    "password": "NewSecurePass456!"
  }'
```

**Expected Response:**
```json
{
  "success": true,
  "message": "Organization updated successfully",
  "organizationName": "Tech Solutions Global",
  "collectionName": "orgTechsolutionsglobal"
}
```

---

## 6. Delete Organization

**Requires Authentication!**

```bash
curl -X DELETE "$BASE_URL/org/delete?organizationName=Tech%20Solutions%20Global" \
  -H "Authorization: Bearer $TOKEN"
```

**Expected Response:**
```json
{
  "success": true,
  "message": "Organization deleted successfully"
}
```

---

## Complete Test Flow

Run all commands in sequence:

```bash
# 1. Set base URL
export BASE_URL=http://localhost:8000

# 2. Health check
echo "=== Health Check ==="
curl $BASE_URL/

# 3. Create organization
echo -e "\n\n=== Create Organization ==="
curl -X POST $BASE_URL/org/create \
  -H "Content-Type: application/json" \
  -d '{
    "organizationName": "Demo Corp",
    "email": "admin@democorp.com",
    "password": "demo123456"
  }'

# 4. Login and get token
echo -e "\n\n=== Admin Login ==="
LOGIN_RESPONSE=$(curl -s -X POST $BASE_URL/admin/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@democorp.com",
    "password": "demo123456"
  }')

echo $LOGIN_RESPONSE

# Extract token (requires jq)
export TOKEN=$(echo $LOGIN_RESPONSE | jq -r '.token')
echo "Token: $TOKEN"

# 5. Get organization
echo -e "\n\n=== Get Organization ==="
curl "$BASE_URL/org/get?organizationName=Demo%20Corp"

# 6. Update organization
echo -e "\n\n=== Update Organization ==="
curl -X PUT $BASE_URL/org/update \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "organizationName": "Demo Corp",
    "newOrganizationName": "Demo Industries",
    "email": "admin@demoindustries.com",
    "password": "newdemo789"
  }'

# 7. Delete organization
echo -e "\n\n=== Delete Organization ==="
curl -X DELETE "$BASE_URL/org/delete?organizationName=Demo%20Industries" \
  -H "Authorization: Bearer $TOKEN"
```

---

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Organization name already exists"
}
```

### 401 Unauthorized
```json
{
  "detail": "Invalid email or password"
}
```

### 403 Forbidden
```json
{
  "detail": "Not authorized to update this organization"
}
```

### 404 Not Found
```json
{
  "detail": "Organization not found"
}
```

---

## Interactive API Documentation

Visit in browser:
```
http://localhost:8000/docs
```

This provides:
- Interactive API testing
- Request/response schemas
- Try it out feature
- Authentication support

---

## Testing with Postman

1. Import collection from these curl commands
2. Set environment variable `BASE_URL`
3. After login, save `token` as environment variable
4. Use `{{BASE_URL}}` and `{{token}}` in requests

---

## Notes

- Replace `%20` with space in URL-encoded organization names
- Token expires after 24 hours (default)
- All timestamps are in UTC
- Organization names are case-sensitive
