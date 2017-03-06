print("Welcome to the UB vending machine")
coins = int(input("Enter the number of quarters you wish to insert:"))
total_money = float(coins * 0.25)
print("you entered",total_money, "dollars")
print("-----------------------------------")

water_price= 1.0
juice_price= 3.0
soda_price= 1.5
chips_price=1.25
peanut_price=0.75
cookies_price=1.0







def main_menu():
    print("Select category:\n"
      "1.Drinks\n"
      "2.Snacks\n"
      "3.Exit")
    Option = int(input("Select an option:"))
    print("-----------------------------------")
    optional_menu(Option)


def count_money(choice):
    if(choice=="Water"):
        global total_money
        if(total_money < water_price):
            print("you have insufficient money to buy")
            print("-----------------------------------")
            drinks_menu()
            return
        else:
            total_money=total_money-water_price
            print("Vending:Water","You have",total_money,"left")
            print("-----------------------------------")
            drinks_menu()


    elif(choice=="Juice"):
        if(total_money< juice_price):
            print("you have insufficient money to buy")
            print("-----------------------------------")
            drinks_menu()
            return

        else:
            total_money=total_money-juice_price
            print("Vending:Juice","You have",total_money,"left")
            print("-----------------------------------")
            drinks_menu()



    elif(choice=="Soda"):
        if(total_money < soda_price):
            print("you have insufficient money to buy")
            print("-----------------------------------")
            drinks_menu()
            return
        else:
            total_money=total_money-soda_price
            print("Vending:Soda","You have",total_money,"left")
            print("-----------------------------------")
            drinks_menu()


    elif(choice=="Chips"):
        if(total_money < chips_price):
            print("you have insufficient money to buy")
            print("-----------------------------------")
            snacks_menu()
            return
        else:
            total_money=total_money-chips_price
            print("Vending:Chips","You have",total_money,"left")
            print("-----------------------------------")
            snacks_menu()

    elif(choice=="Peanuts"):
        if(total_money < peanut_price):
            print("you have insufficient money to buy")
            print("-----------------------------------")
            snacks_menu()
            return
        else:
            total_money=total_money-peanut_price
            print("Vending:Peanuts","You have",total_money,"left")
            print("-----------------------------------")
            snacks_menu()

    elif(choice=="Cookies"):
        if(total_money < cookies_price):
            print("you have insufficient money to buy")
            print("-----------------------------------")
            snacks_menu()
            return
        else:
            total_money=total_money-cookies_price
            print("Vending:Cookies","You have",total_money,"left")
            print("-----------------------------------")
            snacks_menu()


def snacks_menu():
    print("Chips <$1.25>\n"
          "Peanuts <$0.75>\n"
          "Cookies <$1.0>\n")
    choice = input("Enter your snacks selection <x to exit>")
    print("-----------------------------------")

    if choice=="x":
        main_menu()
    elif choice=="Chips":
        count_money(choice)

    elif choice=="Peanuts":
        count_money(choice)
    elif choice=="Cookies":
        count_money(choice)
    else:

        print("Invalid selection")
        print("-----------------------------------")
        snacks_menu()




def drinks_menu():
    print("Water <$1>\n"
          "Juice <$3>\n"
          "Soda <$1.5>\n")
    choice = input("Enter your drink selection <x to exit>")
    print("-----------------------------------")

    if choice=="x":
        main_menu()
    elif choice=="Water":
        count_money(choice)

    elif choice=="Juice":
        count_money(choice)
    elif choice=="Soda":
        count_money(choice)
    else:

        print("Invalid selection")
        print("-----------------------------------")
        drinks_menu()





def optional_menu(Option):

    if Option == 1:
        drinks_menu()
    elif Option==2:
        snacks_menu()
    elif Option==3:
        print("Good Bye","Your total remaining amount is",total_money)
        wait=input("Press enter to continue:")
    else:
        print("Invalid selection please try again")
        print("-----------------------------------")
        main_menu()

print("Select category:\n"
      "1.Drinks\n"
      "2.Snacks\n"
      "3.Exit")
Option = int(input("Select an option:"))
print("-----------------------------------")
optional_menu(Option)