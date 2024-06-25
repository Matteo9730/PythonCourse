import random


class MyException(Exception):
    pass


def get_user_input(prompt, valid_options=None, error_message="Invalid input"):
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


def place_bet(cash):
    while True:
        quantity = get_user_input(f"How much do you want to bet? Remember, between 1 and {cash}: ",
                                  error_message=f"You should choose between 1 and {cash}")
        if 1 <= quantity <= cash:
            return quantity


def choose_horse():
    return get_user_input("Now, you have to choose the horse, from 1 to 10: ", range(1, 11),
                          "You should choose between 1 and 10")


def run_race():
    return random.sample(range(1, 11), 3)


def display_winners(winners):
    print(f"""Here are the winners:
    First place: {winners[0]}
    Second place: {winners[1]}
    Third place: {winners[2]}
    """)


def betting_game():
    print("Welcome")
    cash = 100

    while cash > 0:
        play = get_user_input("Do you want to play?\n1. Yes\n2. No\n", [1, 2], "You should choose 1 or 2")
        if play == 2:
            print("Bye")
            break

        print(f"You have {cash} €")
        type_bet = get_user_input(
            "You want to bet on the placed or on the winner?\n1. On the placed\n2. On the winner\n",
            [1, 2], "You should choose 1 or 2")
        money = get_user_input(
            "Do you want to choose your own bet or the computer chooses for you (5€)?\n1. I want to choose how much to bet\n2. The computer chooses for me\n",
            [1, 2], "You should choose 1 or 2")

        quantity = 5 if money == 2 else place_bet(cash)
        horse = choose_horse()

        print("It's time to play!")
        winners = run_race()
        display_winners(winners)

        if type_bet == 1:  # On the placed
            if horse in winners:
                print("Wow! You won")
                cash += (quantity * 2)
            else:
                print("Oh no! You lost")
                cash -= quantity
        else:  # On the winner
            if horse == winners[0]:
                print("Wow! You won")
                cash += (quantity * 5)
            else:
                print("Oh no! You lost")
                cash -= quantity

        print(f"Now you have {cash} €")

    if cash <= 0:
        print("You have no money! Bye")


if __name__ == "__main__":
    betting_game()