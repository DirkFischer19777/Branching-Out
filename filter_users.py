import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)
def filter_users_by_age(min_age, max_age=None):
    """
    Filtert Benutzer nach Alter.
    - min_age: Mindestalter
    - max_age: optional, Maximalalter
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    if max_age is not None:
        filtered_users = [user for user in users if min_age <= user["age"] <= max_age]
    else:
        filtered_users = [user for user in users if user["age"] == min_age]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (name/age): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        min_age = int(input("Enter the minimum age: "))
        max_age_input = input("Enter the maximum age (press Enter to skip): ").strip()
        max_age = int(max_age_input) if max_age_input else None
        filter_users_by_age(min_age, max_age)
    else:
        print("Filtering by that option is not yet supported.")