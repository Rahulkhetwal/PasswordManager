# Password Manager

A simple yet secure **Password Manager** application built using Python. This project allows users to store, retrieve, and manage their passwords efficiently, with all sensitive data encrypted using **AES-256 encryption** for maximum security.

---

## 🔒 **Key Features**
- **Store Credentials**: Save website credentials (username and password) securely.
- **Retrieve Credentials**: Access your stored credentials quickly.
- **Secure Encryption**: Implements AES-256 encryption to protect your passwords.
- **User-Friendly Interface**: Simple terminal-based interaction for easy use.

---

## 🛠️ **Technologies Used**
- **Python**: Core programming language.
- **PyCryptodome**: Library used for AES encryption and decryption.
- **JSON**: File-based storage for encrypted data.

---

## ⚙️ **Installation and Setup**
1. **Clone the Repository**:
   ```bash
   git clone <your-repo-url>
   cd PasswordManager

2. **Install Dependencies**: 
   Ensure Python 3.x is installed.   Then,install the required library:
   ```bash
   pip install pycryptodome

3. **Run the Application**: 
   Start the program by running:
   ```bash
   python main.py


🖥️ How to Use

1.Save a Password:

    Choose the "Save Password" option from the menu.
    Enter the website name, username, and password to store.

2.Retrieve a Password:

    Choose the "Retrieve Password" option.
    Enter the website name to view its saved credentials.

3.Exit:

    Select "Exit" from the menu to close the application.


📂 Project Structure

PasswordManager/
├── main.py               # Main script for user interaction
├── encryption_utils.py   # Encryption and decryption logic
├── passwords.json        # Encrypted password storage
├── README.md             # Project documentation

💻 Example Interaction

## Saving a Password:
Password Manager
1. Save Password
2. Retrieve Password
3. Exit
Choose an option: 1
Enter website: example.com
Enter username: user123
Enter password: pass@123
Password saved successfully!

## Retrieving a Password:
Password Manager
1. Save Password
2. Retrieve Password
3. Exit
Choose an option: 2
Enter website: example.com
Website: example.com
Username: user123
Password: pass@123

🔐 Security Details

#Encryption: All passwords are encrypted using AES-256 before being stored.

#Decryption: Passwords are decrypted only when retrieved by the user.

#Storage: Encrypted credentials are stored in passwords.json.

⚠️ Note: Keep the encryption key in encryption_utils.py secret to ensure data security.


🚀 Future Enhancements

1.Add a graphical user interface (GUI) for better usability.
2.Implement a Master Password to restrict access to the manager.
3.Support export and import of credentials.
4.Enable password strength analysis during creation.


📄 License

This project is developed as part of an academic minor project and is for educational purposes only.

👨‍💻 Contributors
[Rahul Khetwal]
Feel free to contribute by submitting issues or pull requests!


