import json

file_name = "data.json"

def load_data():
    with open(file_name,"r", encoding = "utf-8") as file:
        return json.load(file)
    
def save_data(tasks):
    with open(file_name,"w",encoding = "utf-8") as file:
        json.dump(tasks,file,ensure_ascii=False,indent=2)   
