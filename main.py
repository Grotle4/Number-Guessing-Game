import random
import time
import math



print("Welcome to the number guessing game!")
guess_correct = False
is_playing = True
number_list = []
score_easy = None
score_medium = None #Establish all variable
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
    match user_diff:                #Function to determine difficulty of the round
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
        return "Below range" #Function to determine if the number value inputted is between 1 and 100
    else:
        return "Above range"
    
def restart_game():
    play_again = input("Would you like to begin a new round? ").lower()
    match play_again:
        case "yes":
            print("You will begin the next round!")
            print("")
            return True            #Function to restart the game after successfully winning or losing
        case "no":
            print("Game Over!")
            return False
        case _ :
            print("Not a valid command")

def select_number(chances, start_time, difficulty):
    random_num = random.randint(1,100) #Creates random number
    while chances > 0: #Will continue to run until out of attempts
        try:
            print("")
            print(f"You have {chances} attempts remaining.")
            print(f"Current numbers guessed: ", *number_list)
            if chances == 1:
                closest_number = check_list(number_list, random_num)
                print(f"Your closest guess has been {closest_number}") #Hint system, will reveal closest number on the final attempt
            selected_num = int(input("Please select a number between 1 and 100: "))
            is_dupp = check_duplicate(number_list, selected_num) #Checks to make sure no dupplicate number is selected
            if is_dupp != True:
                number_list.append(selected_num)
            value_range = check_range(selected_num, 1, 100) # Takes the value of the selected number, will return a string determining if the value is within the range or not
            match value_range:
                case "Within range": #As long as the number is within the range
                    if selected_num == random_num:
                        print("")
                        print("That is correct, yippie :D") #Will run if the answer is correct
                        elasped_time = math.ceil(time.time() - start_time) #Takes down the time between selecting difficulty and the answer being found
                        number_list.clear() #Clears the list of all prior answers
                        game_timer(elasped_time) #Will take the game time and format it properly based on if it was minutes or seconds
                        check_score(chances, difficulty) #Checks the user score and will update if the current value is a high score or not, lower is a higher score
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
    number_list.clear()
    return restart_game()

def game_timer(end_time):
    match end_time:
        case 1:
            print(f"You took {end_time} second to get the answer!") #Determines the best grammer when referring to second or seconds
        case _ if end_time in range(2,60):  
            print(f"You took {end_time} seconds to get the answer!")  
        case _ if end_time >= 60:
            print(end_time)
            minutes = math.floor(end_time / 60)
            seconds = (end_time - (minutes * 60))  #Takes the time in seconds and will subtract the multiple of 60 in reference to the number of minutes to get remaining seconds
            if minutes == 1: 
                print(f"You took {minutes} minute and {seconds} seconds to get the answer!") #Determines the best grammer when referring to miunte or minutes
            else:
                print(f"You took {minutes} minutes and {seconds} seconds to get the answer!")

def check_list(number_list, random_num):
    closest_number = min(number_list, key=lambda x: abs(x - random_num)) #Determines which number in the list is closest for hint function
    return closest_number

def check_score(chances, difficulty): 
    hard_chances = 3
    medium_chances = 5
    easy_chances = 10

    global score_easy
    global score_medium
    global score_hard

    match difficulty:
        case "easy":
            score = ((chances - 1)- easy_chances) * -1 #Takes the number of chances remaining and subtracts them by the base chance value, flip the negative and return that as score       
            if score_easy is None or score_easy > score: #Is none is used in case there is no high score to compare to at the start of the game
                score_easy = score #Will update the score based on difficulty
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
            

def check_duplicate(number_list, selected_num): #Iterates through loop and will return a true value to is_dupp variable to show a dupplicate has been found
    for item in number_list:
        if item == selected_num:
            print("You have already selected this number, try again!")
            return True


while is_playing: #Game loop, will return is_playing = False when any lose or quit conditions have been met
    try:
        chances, start_time, difficulty = check_difficulty()
        is_playing = select_number(chances, start_time, difficulty) #Returns a true or false value from the function, as long as the value remains true, the function will continue to exist
    except:
        pass
