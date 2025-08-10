# Meal Calorie Count Generator

## Objective
A backend service built with FastAPI that allows users to input a dish name and number of servings, then returns the total calorie count using the free USDA FoodData Central API. Includes authentication, PostgreSQL integration, and fuzzy matching for food search.

---

## 📦 Tech Stack
- **Language:** Python (FastAPI)
- **Database:** PostgreSQL
- **External API:** USDA FoodData Central API
- **Authentication:** JWT-based
- **Hosting (Optional):** Render, Railway, Vercel, or local server

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd meal-calorie-backend
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the project root:
```env
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<database_name>
USDA_API_KEY=your_usda_api_key_here
JWT_SECRET=your_jwt_secret_here
JWT_ALGORITHM=HS256
```

**Note:**
- `JWT_SECRET` can be any strong random string (e.g., generated via `openssl rand -hex 32`).
- `JWT_ALGORITHM` is usually `HS256`.

Also create `.env.example` for reference (do not include secrets).

### 5️⃣ Setup PostgreSQL Database
Login to PostgreSQL:
```bash
psql -U postgres
```
Create database & table:
```sql
CREATE DATABASE meal_calorie_db;

\c meal_calorie_db

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);
```

### 6️⃣ Run the Server
```bash
uvicorn app.main:app --reload
```
API will be live at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 7️⃣ Test in Postman
**Auth Endpoints:**
- **POST** `/auth/register`
```json
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "password": "StrongPass123!"
}
```
- **POST** `/auth/login`
```json
{
    "email": "john@example.com",
    "password": "StrongPass123!"
}
```

**Main Endpoint:**
- **POST** `/get-calories`  
Headers: `Authorization: Bearer <token>`  
Body:
```json
{
    "dish_name": "chicken biryani",
    "servings": 2
}
```

---

## 📌 Design Decisions
- Used **FastAPI** for speed and automatic documentation generation.
- JWT for stateless authentication.
- PostgreSQL for structured data storage.
- Fuzzy matching via `rapidfuzz` for better dish name search.
- `.env` for secure config handling.
- Modular folder structure for maintainability.

---