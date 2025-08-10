from fastapi import FastAPI
from app.auth import routes as auth_routes
from app.calories import routes as calorie_routes
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Meal Calorie Count API")

app.include_router(auth_routes.router)
app.include_router(calorie_routes.router)
