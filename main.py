import random



print("Welcome to the number guessing game!")
random_num = random.randint(1,100)

def check_diffculty():
    user = input("please select a difficulty(easy/medium/hard): ")
    user_diff = user.lower()
    match user_diff:
        case "easy":
            print("easy")
            return 10
        case "medium":
            print("medium")
            return 5
        case "hard":
            print("hard")
            return 3
        case _:
            print("Difficulty selected is invalid")


def select_number():
    global chances
    selected_num = int(input("Please select a number between 1 and 100"))
    if selected_num == random_num:
        print("that is correct, yippie :D")
    elif random_num >= selected_num:
        print(f"The number is greater than {selected_num}")
        chances -= 1
    else:
        print(f"The number is less than {selected_num}")
        chances -= 1


print(random_num)
chances = check_diffculty()
while chances > 0:
    print(f"You have {chances} attemps remaining.")
    select_number()

