import json

def read_json(file_path):
    try:
        with open(file_path, "r",encoding="utf-8") as f:
            data = json.load(f)
            print("Current JSON Data:")
            print(json.dumps(data, indent=4))
            return data
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
def update_json(file_path, key, value):
    data = read_json(file_path)
    if data is None:
        return

    # If JSON is a dictionary
    if isinstance(data, dict):
        data[key] = value

    # If JSON is a list
    elif isinstance(data, list):
        print("\nJSON contains a list.")
        index = int(input("Enter index number to update: "))
        if isinstance(data[index], dict):
            data[index][key] = value
        else:
            print("Selected item is not an object.")

    # Write back to file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("\nUpdated successfully!")

if __name__ == "__main__":
    file = input("Enter JSON file path: ").strip().strip('"')
    read_json(file)
    key = input("Enter key to update: ")
    value = input("Enter new value: ")

    update_json(file, key, value)