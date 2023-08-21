class Users:
    def __init__(self):
        self.users = {}

    def sign_in(self):
        try:
            name = input("Enter the Name: ")
            password = input("Enter the password: ")
            self.users[name] = password
            print("User registered successfully! Well done!")
        except Exception as e:
            print(f"Error: {str(e)}")

    def show_users(self):
        print("Registered users:")
        for name, password in self.users.items():
            print(f"Username: {name} | Password: {password}")

    def login(self):
        try:
            name = input("Enter the username: ")
            password = input("Enter the password: ")
            if name in self.users and self.users[name] == password:
                print("You are logged in!")
            else:
                print("Invalid login credentials.")
        except Exception as e:
            print(f"Error Log In: {str(e)}")

    def save_users(self):
        try:
            with open("users.txt", "w") as file:
                for name, password in self.users.items():
                    file.write(f"{name},{password}\n")
            print("Users saved!")
        except Exception as e:
            print(f"Error : {str(e)}")

    def load_users(self):
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    name, password = line.strip().split(",")
                    self.users[name] = password
            print("Users loaded successfully!")
        except FileNotFoundError:
            print("Creating a new user database.")
        except Exception as e:
            print(f"Error: {str(e)}")

# Crear una instancia de la clase Users fuera de la clase
user_manager = Users()
user_manager.load_users()

# Diccionario para almacenar los usuarios (nombre: contraseña)
usuarios = user_manager.users