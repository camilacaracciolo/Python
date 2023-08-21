from usuarios import *
from comprador import *
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
    
        
    client_obj = Client(name, email, address, money)
    clientes.append(client_obj)
    
    print(f"Client '{name}' created successfully!")

while True:
    print("\nMenu")
    print("\n1- Sign In")
    print("\n2- Show User List")
    print("\n3- Login")
    print("\n4- Save Users")
    print("\n5- Create Client")
    print("\n6- Buy")
    print("\n7- Recharge Money")
    print("\n8- Exit")
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
