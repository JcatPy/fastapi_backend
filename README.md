# 🧪 FastAPI Backend Project

A backend web application using FastAPI, SQLModel, and PostgreSQL, implementing full CRUD operations for users and posts.

## 🚀 Features
- FastAPI framework with modular routing
- SQLModel (SQLAlchemy + Pydantic) for ORM and validation
- PostgreSQL for database
- Secure password hashing
- Auto-generated Swagger docs


## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/JcatPy/fastapi_backend.git
cd fastapi_backend
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scriptsctivate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
uvicorn app.main:app --reload
```

### 5. API Documentation
- Swagger UI: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

## 🧪 API Routes

### `/posts`
- `GET /posts`: Get all posts
- `POST /posts`: Create a new post
- `GET /posts/{id}`: Get a specific post
- `PUT /posts/{id}`: Update a post
- `DELETE /posts/{id}`: Delete a post

### `/users`
- `POST /users`: Create a new user
- `GET /users/{id}`: Get user by ID

## 🛡️ Security
- Passwords are hashed using a utility function (`hash_password`)
- Uses SQLModel’s validation for input safety

## 📦 Optional Enhancements
- JWT Authentication
- Role-based access (admin/user)
- Pagination and filtering
- Dockerize the app for deployment

## 📜 License
MIT
