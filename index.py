from users import Users, Client

# Crear una instancia de la clase Users
user_manager = Users()

# Diccionario para almacenar los usuarios (nombre: contraseña)
usuarios = user_manager.users

# Lista para almacenar clientes
clientes = []

def create_client():
    name = input("Enter the client's name: ")
    email = input("Enter the client's email: ")
    address = input("Enter the client's address: ")
    money = int(input("Enter the client's initial amount of money: "))
    
    # Crear instancia de Cliente y agregarla a la lista
    client_obj = Client(name, email, address, money)
    clientes.append(client_obj)
    
    print(f"Client '{name}' created successfully!")

while True:
    print("\nMenu")
    print("1- Sign In")
    print("2- Show User List")
    print("3- Login")
    print("4- Save Users")
    print("5- Create Client")
    print("6- Buy")
    print("7- Recharge Money")
    print("8- Exit")
    selection = input("Enter an option: ")

    if selection == "1":
        user_manager.sign_in()
    elif selection == "2":
        user_manager.show_users()
    elif selection == "3":
        user_manager.login()
    elif selection == "4":
        user_manager.save_users()
    elif selection == "5":
        create_client()
    elif selection == "6":
        client_name = input("Enter your name: ")
        found_client = None
        for client in clientes:
            if client.name == client_name:
                found_client = client
                break

        if found_client:
            amount = float(input("Enter the amount to buy: "))
            found_client.buy(amount)
        else:
            print("Please register first.")
    elif selection == "7":
        client_name = input("Enter your name: ")
        found_client = None
        for client in clientes:
            if client.name == client_name:
                found_client = client
                break

        if found_client:
            amount = float(input("Enter the amount to recharge: "))
            found_client.recharge_cash(amount)
        else:
            print("Please register first.")
    elif selection == "8":
        break
    else:
        print("Invalid option. Please try again.")

print("That's all, my friends!")
