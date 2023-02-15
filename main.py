import requests
from datetime import datetime
APP_ID="a2a8a773"
API_KEY="5c36abce3365f306d6cb796ee228c583"
GENDER = "F"
WEIGHT_KG = 65
HEIGHT_CM = 175.26
AGE = 32
headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,

}
exercise_text=input("which exercise have you done today?")
nutrition_parameters={
    "query":exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE    
}
exercise_endpoint=" https://trackapi.nutritionix.com/v2/natural/exercise"
response=requests.post(url=exercise_endpoint,json=nutrition_parameters,headers=headers)
result=response.json()
# print(result)

sheety_endpoint="https://api.sheety.co/c17c927a9220b5060a269000ebd594fb/myWorkouts/workouts"
today=datetime.now()
today_date=today.strftime("%d/%m/%Y")
today_time=today.strftime("%X")
for exercise in result["exercises"]:
    sheet_input={
        "workout":[
            {
            "date":today_date,
            "time":today_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
        ]
    }
responses=requests.post(url=sheety_endpoint,json=sheet_input)
print(responses.text)