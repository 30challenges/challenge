numbers = []

for i in range(3):
    entry = float(input("Enter a number: "))
    numbers.append(float(entry))

print(f"Numbers entered: {numbers}")
print(f"Largest number: {max(numbers)}")