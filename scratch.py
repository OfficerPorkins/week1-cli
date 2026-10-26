tasks = [
    {"title": "buy milk", "done": False},
    {"title": "call mom", "done": True},
]

for task in tasks:
    mark = "x" if task["done"] else " "
    print(f"[{mark}] {task['title']}")

tasks[0]["done"] = True

for task in tasks:
    mark = "x" if task["done"] else " "
    print(f"[{mark}] {task['title']}")