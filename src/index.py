from user import User
from budget import Budget

def main():
    name = input("anna käyttäjänimi: ")
    psw = input("anna salasana: ")
    budger = Budget()
    order =""
    while True:
        print("Master of my earnings, enlighten my spirit with your orders ")
        print("1: to add cost")
        print("2: To stop me embarassing You and let me slumber to a cave ")
        print("3: for your wishes: ")
        order = int(input("Shall i get my order? "))
        if order == 1:
            costco = input("Sire please provide me with your desire: ")
            money = (input("Please give spent amount: "))
            budger.add_cost(costco, money)
        if order == 2:
            break
        if order == 3:
            list = budger.return_items()
            for line in list:
                print(line)

    user_x = User(name, psw)
    print(user_x)


if __name__ == "__main__":
    main()