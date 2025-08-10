import requests
from fuzzywuzzy import fuzz
from app.core.config import settings

USDA_BASE_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

class CalorieService:
    @staticmethod
    def get_calories(dish_name: str, servings: int):
        params = {
            "query": dish_name,
            "api_key": settings.USDA_API_KEY,
            "pageSize": 10
        }
        response = requests.get(USDA_BASE_URL, params=params)
        if response.status_code != 200:
            return None
        
        data = response.json()
        if not data.get("foods"):
            return None

        best_match = max(data["foods"], key=lambda food: fuzz.token_sort_ratio(dish_name.lower(), food["description"].lower()))
        
        nutrients = best_match.get("foodNutrients", [])
        calories_per_serving = next((n["value"] for n in nutrients if n["nutrientName"].lower() == "energy"), None)
        
        if calories_per_serving is None:
            return None
        
        total_calories = calories_per_serving * servings
        return {
            "dish_name": dish_name,
            "servings": servings,
            "calories_per_serving": calories_per_serving,
            "total_calories": total_calories,
            "source": "USDA FoodData Central"
        }
