import random


print("Welcome to the number guessing game!")

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

chances = check_diffculty()


random_num = random.randint(1,100)
print(random_num)

