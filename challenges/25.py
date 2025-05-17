tocount = str(input("Enter a string: "))
vowels = "aeiou"

def count(string):
    amount = 0
    for char in string.lower():
        if char in vowels:
            amount += 1
    return amount

print(f"There are {count(tocount)} vowel(s) in the string.")