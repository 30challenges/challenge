num1 = float(input("Enter a number. "))
num2 = float(input("Enter another number. "))
option = str(input("Enter function you would like to perform. (add, subtract, divide, multiply) "))

if option == "add":
    print(f"{num1} + {num2} = {num1 + num2}.")
elif option == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}.")
elif option == "divide":
    print(f"{num1} / {num2} = {num1 / num2}.")
elif option == "multiply":
    print(f"{num1} x {num2} = {num1 * num2}.")