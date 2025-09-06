import json


def filter_users_by_name(name):
    """
        Filtert Benutzer aus users.json anhand ihres Namens (case-insensitive).

        Args:
            name (str): Name des Benutzers, nach dem gefiltert werden soll.
    """

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

def filter_users_by_email(email):
    """
        Filtert Benutzer aus users.json anhand ihrer E-Mail-Adresse (case-insensitive).

        Args:
            email (str): E-Mail-Adresse, nach der gefiltert werden soll.
    """

    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)


def main():
    """Fragt den Benutzer nach Filterkriterien und führt die passende Funktion aus."""

    filter_option = input("What would you like to filter by? (name/age/email):  ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        min_age = int(input("Enter the minimum age: "))
        max_age_input = input("Enter the maximum age (press Enter to skip): ").strip()
        max_age = int(max_age_input) if max_age_input else None
        filter_users_by_age(min_age, max_age)

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)

    else:
        print("Filtering by that option is not yet supported.")

if __name__ == "__main__":
    main()