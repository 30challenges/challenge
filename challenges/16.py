import random

sides = int(input("How many sides of the dice? "))
result = random.randint(1, sides)

print("You roll the dice.")
print(f"It lands on a {result}.")

if result >= sides / 2:
    print("You win.")
else:
    print("You lose.")
