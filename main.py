import random



print("Welcome to the number guessing game!")
guess_correct = False
is_playing = True

def check_diffculty():
    print("Please select a difficulty level:")
    print("Easy   (10 chances)")
    print("Medium (5 chances)")
    print("Hard   (3 chances)")
    user = input("Please input a difficulty: ")
    user_diff = user.lower()
    match user_diff:
        case "easy":
            print("You have selected easy difficulty")
            return 10
        case "medium":
            print("You have selected medium difficulty")
            return 5
        case "hard":
            print("You have selected hard difficulty")
            return 3
        case _:
            print("Difficulty selected is invalid, please select Easy, Medium or Hard")

def check_range(number, start, stop):
    if number in range(start,stop):
        return "Within range"
    elif number < start:
        return "Below range"
    else:
        return "Above range"
    
def restart_game(is_still_playing):
    play_again = input("Would you like to begin a new round?").lower()
    match play_again:
        case "yes":
            print("You will begin the next round!")
            chances = check_diffculty()
            select_number(chances,is_playing)
            is_still_playing = True
            return is_still_playing
        case "no":
            print("game is over")
            is_still_playing = False
            return is_still_playing
        case _ :
            print("not a valid command")

def select_number(chances,start_playing):
    random_num = random.randint(1,100)
    print(random_num)
    if start_playing == True:
        while chances > 0:
            try:
                print("")
                print(f"You have {chances} attemps remaining.")
                selected_num = int(input("Please select a number between 1 and 100: "))
                value_range = check_range(selected_num, 1, 100)
                match value_range:
                    case "Within range":
                        if selected_num == random_num:
                            print("that is correct, yippie :D")
                            start_playing = restart_game(is_playing)
                        elif random_num >= selected_num:
                            print(f"The number is greater than {selected_num}")
                            chances -= 1
                        elif random_num <= selected_num:
                            print(f"The number is less than {selected_num}")
                            chances -= 1
                    case "Above range":
                        print("This number is greater than 100, Try again")
                        continue
                    case "Below range":
                        print("This number is below than 100, Try again")
                        continue
            except ValueError:
                print("Value selected is not a whole number, try again")
    else:
        pass

chances = check_diffculty()
select_number(chances,is_playing)

