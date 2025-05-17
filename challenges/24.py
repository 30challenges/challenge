txt = str(input("Enter a string: "))

reversed = txt[::-1]
print(f"Reversed: {reversed}")

# removes spaces from strings incase the palindrome is more than 1 word
nospace = reversed.replace(" ", "")
nospacetxt = txt.replace(" ", "")

if nospace == nospacetxt:
    print("String is a palindrome.")
else:
    print("String is not a palindrome.")