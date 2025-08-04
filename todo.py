tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def show_tasks():
    for i, t in enumerate(tasks):
        status = "✅" if t["done"] else "❌"
        print(f"{i+1}. {status} {t['task']}")

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

# Demo
add_task("Learn Git")
add_task("Write Python script")
mark_done(0)
show_tasks()
