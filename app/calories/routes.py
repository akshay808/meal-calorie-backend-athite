from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, conint
from app.calories.service import CalorieService

router = APIRouter(tags=["Calories"])

class CalorieRequest(BaseModel):
    dish_name: str
    servings: conint(gt=0)

@router.post("/get-calories")
def get_calories(req: CalorieRequest):
    result = CalorieService.get_calories(req.dish_name, req.servings)
    if not result:
        raise HTTPException(status_code=404, detail="Dish not found or calorie data unavailable")
    return result
