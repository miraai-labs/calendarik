import json

file_name = "data.json"

def load_data():
    with open(file_name,"r", encoding = "utf-8") as file:
        return json.load(file)
    
