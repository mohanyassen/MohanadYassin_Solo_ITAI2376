from src.agent import run_agent

print("Smart Health Assistant AI 🤖")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: Stay healthy! 👋")
        break

    response = run_agent(user_input)
    print("Agent:", response)