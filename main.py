import random



print("Welcome to the number guessing game!")
random_num = random.randint(1,100)
guess_correct = False

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

def select_number(chances):
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
                        break #add loopable functionality
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

print(random_num)
chances = check_diffculty()
select_number(chances)

