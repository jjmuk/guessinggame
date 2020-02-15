# Guessing game
import random
g_number = int(input("Enter guess number: "))
r_number = random.randint(1, 10)
if g_number < r_number:
    print("Wrong, try again")
if g_number > r_number:
    print("Wrong, try again")
if g_number == r_number:
    print("Correct!")




