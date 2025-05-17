numbers = []

while True:
    entry = input("Enter a number (or type 'done' to stop): ")
    if entry == "done":
        break
    else:
        numbers.append(int(entry))

print(f"Numbers entered: {numbers}")
print(f"Sum of numbers = {sum(numbers)}")