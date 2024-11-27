import json
from encryption_utils import encrypt, decrypt

DATA_FILE = "passwords.json"

def load_data():
    """Loads password data from the JSON file."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    """Saves password data to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def save_password(website, username, password):
    """Saves a new encrypted password."""
    data = load_data()
    data[website] = {"username": username, "password": encrypt(password)}
    save_data(data)
    print("Password saved successfully!")

def retrieve_password(website):
    """Retrieves and decrypts a password for the given website."""
    data = load_data()
    if website in data:
        entry = data[website]
        print(f"Website: {website}")
        print(f"Username: {entry['username']}")
        print(f"Password: {decrypt(entry['password'])}")
    else:
        print("Website not found!")

def main():
    while True:
        print("\nPassword Manager")
        print("1. Save Password")
        print("2. Retrieve Password")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            save_password(website, username, password)

        elif choice == "2":
            website = input("Enter website: ")
            retrieve_password(website)

        elif choice == "3":
            print("Exiting Password Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
