from src.tools import nutrition_tool, health_advice_tool
from src.memory import save_memory, load_memory

def run_agent(user_input):
    text = user_input.lower()
    memory = load_memory()

    # store simple info
    if "weight" in text:
        save_memory("weight", user_input)
        return "Got it — I saved your weight."

    if "sleep" in text:
        save_memory("sleep", user_input)
        return "Got it — I saved your sleep info."

    # tool 1
    if any(word in text for word in ["calories", "eat", "food"]):
        return nutrition_tool(user_input)

    # tool 2
    if any(word in text for word in ["tired", "stress", "headache"]):
        return health_advice_tool(user_input, memory)

    # SMART fallback (NEW UPGRADE)
    return (
        "I can help you with nutrition, sleep, stress, and general wellness. "
        "Try asking something like: 'How many calories in an orange?' or 'I feel tired'"
    )