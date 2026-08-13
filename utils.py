import json
# Load data from a JSON file.
def load(filename):
    try:
        with open(filename , "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("File not found!")
    except json.JSONDecodeError:
        print("Invalid json file!")
# Save data to a JSON file.
def save(filename,data):
    try:
        with open(filename , "w") as file:
            json.dump(data,file,indent=4)
    except TypeError:
        print("Data cannot be saved!")
    