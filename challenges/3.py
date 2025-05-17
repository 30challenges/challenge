# made this a bit extra so it can add decimals to decimals as well as to whole numbers

# checks if it is an integer, if not, checks if a float, if not, return
def trier(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return

num1ask = input("Enter a number: ")
num2ask = input("Enter another number: ")

num1 = trier(num1ask)
num2 = trier(num2ask)

# if neither inputs are actual numbers
if num1 is None or num2 is None:
    print("Invalid input.")
else:
    print(f"The sum of the numbers is {num1 + num2}.")
