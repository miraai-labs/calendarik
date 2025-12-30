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