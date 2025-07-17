import random
import time
import math



print("Welcome to the number guessing game!")
guess_correct = False
is_playing = True

def check_difficulty():
    print("Please select a difficulty level:")
    print("Easy   (10 chances)")
    print("Medium (5 chances)")
    print("Hard   (3 chances)")
    user = input("Please input a difficulty: ")
    start_time = time.time()
    user_diff = user.lower()
    match user_diff:
        case "easy":
            print("")
            print("You have selected easy difficulty")
            return 10, start_time
        case "medium":
            print("")
            print("You have selected medium difficulty")
            return 5, start_time
        case "hard":
            print("")
            print("You have selected hard difficulty")
            return 3, start_time
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
    play_again = input("Would you like to begin a new round? ").lower()
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

def select_number(chances, start_time):
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
                        elasped_time = math.ceil(time.time() - start_time)
                        game_timer(elasped_time)
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

def game_timer(end_time):
    match end_time:
        case 1:
            print(f"You took {end_time} second to get the answer!")
        case _ if end_time in range(2,60):  
            print(f"You took {end_time} seconds to get the answer!")  
        case _ if end_time >= 60:
            print(end_time)
            minutes = math.floor(end_time / 60)
            seconds = (end_time - (minutes * 60))
            if minutes == 1:
                print(f"You took {minutes} minute and {seconds} seconds to get the answer!")
            else:
                print(f"You took {minutes} minutes and {seconds} seconds to get the answer!")

while is_playing:
    chances, start_time = check_difficulty()
    is_playing = select_number(chances, start_time)

## Need to add still, timer, hint system, user high score