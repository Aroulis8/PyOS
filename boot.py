import os, time, home

username = input("\nPlease enter a username:")
password = input("\nPlease enter a password:")

def start():
    os.system("cls")
    print("Welcome to PyOS.")
    
    print(username)
    os.system("cls")
    
    print(password)
    os.system("cls")
    print("Loading...")
    time.sleep(2)
    home.home()