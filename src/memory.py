import json
import os

FILE = "memory.json"

def load_memory():
    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r") as f:
        return json.load(f)

def save_memory(key, value):
    memory = load_memory()
    memory[key] = value

    with open(FILE, "w") as f:
        json.dump(memory, f)