import random

proteins = ["beans", "omena", "lentils", "tofu", "chicken (once a week)"]
carbs = ["brown rice", "sweet potatoes", "ugali", "cassava"]
veggies = ["cabbage", "spinach", "managu", "terere", "sukuma wiki"]
fruits = ["pawpaw", "avocado", "banana", "oranges"]

sensitive_to_sukuma = input("Do you want to avoid sukuma wiki? (yes/no): ").strip().lower()
if sensitive_to_sukuma == "yes":
    veggies = [veggie for veggie in veggies if veggie != "sukuma wiki"]

def generate_meal_plan():
        return {
            "proteins": random.choice(proteins),
            "carbs": random.choice(carbs),
            "veggies": random.choice(veggies),
            "fruits": random.choice(fruits)
        }
    
meal = generate_meal_plan()
for key, value in meal.items():
    print(f"  {key.title()}: {value}")

while True:
    veggies = ["cabbage", "spinach", "managu", "terere", "sukuma wiki"]
    another = input("Want another meal suggestion? (yes/no): ").strip().lower()
    if another == "yes":
        sensitive_to_sukuma = input("Do you want to avoid sukuma wiki? (yes/no): ").strip().lower()
        if sensitive_to_sukuma == "yes":
            veggies = [veggie for veggie in veggies if veggie != "sukuma wiki"]
        meal = generate_meal_plan()
        print("Here's another meal suggestion:")
        for key, value in meal.items():
            print(f"  {key.title()}: {value}")
    elif another == "no":
        print("Okay, enjoy your meal! 😊")
        break
    else:
        print("Please type 'yes' or 'no'.")
