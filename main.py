import json


def read_coffee_file():
    with open("coffee.json", "r", encoding="CP1251") as data:
        return json.loads(data.read())


def main():
    data = read_coffee_file()
    print(data)


if __name__ == '__main__':
    main()
