def create_task(name,time=None):
    return { 
        "name": name,
        "time": time,
        "done": False,
    }