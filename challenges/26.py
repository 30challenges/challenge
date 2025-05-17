num = int(input("Enter a number: "))

def split(number):
    return [int(digit) for digit in str(number)]

digits = split(num)
print(f"The sum of the digits of the number is {sum(digits)}.")
