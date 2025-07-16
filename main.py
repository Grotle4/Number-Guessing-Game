import random



print("Welcome to the number guessing game!")
guess_correct = False
is_playing = True

def check_difficulty():
    print("Please select a difficulty level:")
    print("Easy   (10 chances)")
    print("Medium (5 chances)")
    print("Hard   (3 chances)")
    user = input("Please input a difficulty: ")
    user_diff = user.lower()
    match user_diff:
        case "easy":
            print("")
            print("You have selected easy difficulty")
            return 10
        case "medium":
            print("")
            print("You have selected medium difficulty")
            return 5
        case "hard":
            print("")
            print("You have selected hard difficulty")
            return 3
        case _:
            print("Difficulty selected is invalid, please select Easy, Medium or Hard")

def check_range(number, start, stop):
    if number in range(start,stop +1):
        return "Within range"
    elif number < start:
        return "Below range"
    else:
        return "Above range"
    
def restart_game():
    play_again = input("Would you like to begin a new round?").lower()
    match play_again:
        case "yes":
            print("You will begin the next round!")
            print("")
            return True
        case "no":
            print("game is over")
            return False
        case _ :
            print("not a valid command")

def select_number(chances):
    random_num = random.randint(1,100)
    print(random_num)
    while chances > 0:
        try:
            print("")
            print(f"You have {chances} attempts remaining.")
            selected_num = int(input("Please select a number between 1 and 100: "))
            value_range = check_range(selected_num, 1, 100)
            match value_range:
                case "Within range":
                    if selected_num == random_num:
                        print("")
                        print("That is correct, yippie :D")
                        print("")
                        return restart_game()
                    elif random_num > selected_num:
                        print("")
                        print(f"The number is greater than {selected_num}")
                        chances -= 1
                    elif random_num < selected_num:
                        print("")
                        print(f"The number is less than {selected_num}")
                        chances -= 1
                case "Above range":
                    print("This number is greater than 100, Try again")
                    continue
                case "Below range":
                    print("This number is below 1, Try again")
                    continue
        except ValueError:
            print("Value selected is not a whole number, try again")
    print(f"Out of chances! The number was {random_num}")
    return restart_game()

while is_playing:
    chances = check_difficulty()
    is_playing = select_number(chances)

