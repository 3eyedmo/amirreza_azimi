import random

MIN_NUMBER = 1
MAX_NUMBER = 5
win_count = 0
game_level = 2
# easy => 1 win
# medium => 2 win
# hard => 3 win

while True:
    level = input("Enter Game Level (easy:e, medium:m, hard:h):  ")
    if level == "e":
        game_level = 1
        print("Game is Easy.")
        break
    elif level == "m":
        game_level = 2
        print("Game is Medium.")
        break
    elif level == "h":
        game_level = 3
        print("Game is Hard.")
        break
    else:
        print("Please select from e, m, h.")
        continue

for i in range(5):
    random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    while True:
        number = input("Enter The Number:  ")
        if number.isnumeric():
            number = int(number)
            if number > MAX_NUMBER or number < MIN_NUMBER:
                print(f"Entered number is not in range {MIN_NUMBER} - {MAX_NUMBER}. Try Again")
                continue
            break
        else:
            print("Sorry. You did not Enter a number.")
            continue

    if random_number == number:
        print("Correct Number.")
        win_count += 1
        
        break
    else:
        print(f"Wrong Number. The number is {random_number}")


if win_count >= game_level:
    print("You win the game.")
else:
    print(f"Sorry, You succeeded for {win_count} times.")