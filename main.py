import json

def load_data(file_path="carepill.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def show_screens(data):
    print(f"Проєкт: {data['project']}")
    print("Екрани додатку:")
    for screen in data["screens"]:
        print(f"- {screen['name']}")

def main():
    data = load_data()
    show_screens(data)

if __name__ == "__main__":
    main()
