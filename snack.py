"""
Mario is a student who has an amount of money set by the user, every day at recess Mario can buy a pastry
at the school cafeteria that costs 1 euro or a sandwich that costs 1.5 euro.
The program continues to ask the user what Mario will eat that day until he has enough money or can satisfy
his appetite with what he wants.
At the end of the program you write in output the number of days when Mario ate and how many times he ate a
pastry and how many times he ate a sandwich
"""
class MyException(Exception):
    pass

def get_user_input(prompt, valid_options = None, error_message="Invalid input"):
    while True:
        try:
            value = int(input(prompt))
            if valid_options and value not in valid_options:
                raise MyException
            return value
        except ValueError:
            print(error_message)
        except MyException:
            print(error_message)

def game():
    days = 0
    pastry = 1
    sandwich = 1.5
    tot_pastry = 0
    tot_sandwich = 0
    print("Welcome")

    money = get_user_input(f"How much money does mario have?: ", error_message="A number and more than 0")
    if money > 1:
        return money

    while money > 0.9:
        play = get_user_input("What should Mario eat?\n1.Pastry\n2.Sandwich\n", [1,2], "You should choose 1 oe 2")
        if play == 1:
            if money < pastry:
                print("Mario doesn't have enough money")
            else:
                print("You choose pastry")
                money -= pastry
                tot_pastry += 1
                days += 1
                print(f"Now Mario has {money}€")
        else:
            if money < sandwich:
                print("Mario doesn't have enough money")
            else:
                print("You choose sandwich")
                money -= sandwich
                tot_sandwich += 1
                days += 1
                print(f"Now Mario has {money}€")
    print("Now Mario doesn't have enough money for the food")
    print(f"You choose {tot_pastry} times pastry, and {tot_sandwich} times sandwich")
    if days <= 1:
        print(f"It's been {days} day")
    else:
        print(f"It's been {days} days")

game()