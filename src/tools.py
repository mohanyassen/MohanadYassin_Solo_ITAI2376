def nutrition_tool(user_input):
    food_data = {
        "banana": 105,
        "apple": 95,
        "pizza": 300,
        "burger": 550,
        "rice": 200,
        "orange": 62,
        "chicken": 165,
        "bread": 80
    }

    for food, calories in food_data.items():
        if food in user_input.lower():
            return f"{food.title()} has about {calories} calories."

    # smarter fallback instead of “I don't know”
    return (
        "I don’t have exact data for that food yet, "
        "but generally whole foods like fruits are low calorie, "
        "and processed foods tend to be higher in calories."
    )


def health_advice_tool(user_input, memory):
    response = []

    text = user_input.lower()

    if "tired" in text:
        response.append("You may need more sleep (7–9 hours).")

    if "stress" in text:
        response.append("Try breathing exercises or short walks.")

    if "headache" in text:
        response.append("Drink water and rest your eyes.")

    response.append("Drink 2–3 liters of water daily.")
    response.append("Light daily exercise improves energy.")

    return " ".join(response)