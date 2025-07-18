import random
import time
import math



print("Welcome to the number guessing game!")
guess_correct = False
is_playing = True
number_list = []
score_easy = None
score_medium = None
score_hard = None
difficulty = None

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
            difficulty = "easy"
            return 10, start_time, difficulty
        case "medium":
            print("")
            print("You have selected medium difficulty")
            difficulty = "medium"
            return 5, start_time, difficulty
        case "hard":
            print("")
            print("You have selected hard difficulty")
            difficulty = "hard"
            return 3, start_time, difficulty
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

def select_number(chances, start_time, difficulty):
    random_num = random.randint(1,100)
    print(random_num)
    while chances > 0:
        try:
            print("")
            print(f"You have {chances} attempts remaining.")
            if chances == 1:
                closest_number = check_list(number_list, random_num)
                print(f"Your closest guess has been {closest_number}")
            selected_num = int(input("Please select a number between 1 and 100: "))
            is_dupp = check_duplicate(number_list, selected_num)
            if is_dupp != True:
                number_list.append(selected_num)
            print(number_list)
            value_range = check_range(selected_num, 1, 100)
            match value_range:
                case "Within range":
                    if selected_num == random_num:
                        print("")
                        print("That is correct, yippie :D")
                        elasped_time = math.ceil(time.time() - start_time)
                        number_list.clear()
                        game_timer(elasped_time)
                        check_score(chances, difficulty)
                        print("score_easy", score_easy)
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

def check_list(number_list, random_num):
    closest_number = min(number_list, key=lambda x: abs(x - random_num))
    return closest_number

def check_score(chances, difficulty):
    print("WORKING SCOre")
    hard_chances = 3
    medium_chances = 5
    easy_chances = 10

    global score_easy
    global score_medium
    global score_hard

    match difficulty:
        case "easy":
            score = ((chances - 1)- easy_chances) * -1
            print("score easy: ", score_easy)
            print("score: ", score)
            if score_easy is None or score_easy > score:
                score_easy = score
                print(f"New easy high score: {score_easy}")
        case "medium":
            score = ((chances - 1)- medium_chances) * -1
            if score_medium is None or score_medium > score:
                score_medium = score
                print(f"New medium high score: {score_medium}")
        case "hard":
            score = ((chances - 1)- hard_chances) * -1
            if score_hard is None or score_hard < score:
                score_hard = score
                print(f"New hard high score: {score_hard}")
            

def check_duplicate(number_list, selected_num):
    for item in number_list:
        if item == selected_num:
            print("You have already selected this number, try again!")
            return True


while is_playing:
    try:
        chances, start_time, difficulty = check_difficulty()
        is_playing = select_number(chances, start_time, difficulty)
    except:
        pass

## Need to work on, fix user high score, always overwriting despte if score is worse. 
# also add prevention of duplicate numbers and do not add scores to list that are over 100 or under 0