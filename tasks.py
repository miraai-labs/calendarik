def create_task(name,time=None):
    return { 
        "name": name,
        "time": time,
        "done": False,
    }
def add_task(tasks,name,time=None):
    task = create_task(name,time)
    tasks.append(task)
    return tasks
def remove_task(tasks,index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return tasks
def mark_done(tasks,index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return tasks    
def is_empty(tasks):
    return len(tasks) == 0