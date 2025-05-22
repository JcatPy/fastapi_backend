# 🧪 FastAPI Backend Project

A backend web application using FastAPI, SQLModel, and PostgreSQL, implementing full CRUD operations for users and posts.

## 🚀 Features
- FastAPI framework with modular routing
- SQLModel (SQLAlchemy + Pydantic) for ORM and validation
- PostgreSQL for database
- Secure password hashing
- Auto-generated Swagger docs

## 🧱 Project Structure
## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/JcatPy/fastapi_backend.git
cd fastapi_backend

### 2. Create Virtual Enviornment
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run the app
uvicorn app.main:app --reload
