import random

print("----Word Guessing Game----")
print()
print("""🙌 you will be shown a random word picked 
from the list we have you will
have to guess it, you have 20 
tries to do so.
Good luck!""")
print("-----------------------------")
print("And here is word enjoy!")
print()


words = random.choice(("peach", "dragonfruit", "watermelon", "mango"))
tries = 20
masked = ["*"] * len(words)

for i in range(len(masked)):
    print(masked[i], end="")
print("\n")

while True:
    whole = input("are you ready to guess the whole word?(y/n): ").lower()

    if whole == "y":
        fullguess = input("Guess the whole word: ").lower()
        tries = tries - 1

        if fullguess == words:
            print("You guessed the word!")
            print(f"The word was {words}!")
            print(f"You have guessed in {tries} tries.")
            print()
            print("Thank you for playing!")
            break

        else:
            print(f"You have {tries} left.")


    elif whole == "n":
        guess = input("Guess a letter: ").lower()
        tries = tries - 1

        if guess in words:
            for i, char in enumerate(words):
                if char == guess:
                    masked[i] = guess

        print(f"tries= {tries}")

        for i in range(len(masked)):
            print(masked[i], end="")
        print()

        flag = False
        if "*" not in masked:
            for i in range(len(masked)):
                if masked[i] == words[i]:
                    flag = True
                    print("You guessed the word!")
                    print(f"The word was {words}!")
                    print(f"You have guessed in {tries} tries.")
                    break

                else:
                    print(f"You have {tries} left.")

        if flag == True:
            print("Thank you for playing!")
            break

    else:
        print("Enter a valid input")