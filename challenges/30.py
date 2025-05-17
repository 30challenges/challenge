numbers = []

while True:
    entry = input("Enter a number (or type 'done' to stop): ")
    if entry == "done":
        break
    else:
        numbers.append(int(entry))

def algorithm(numbers):
    for n in range(len(numbers) - 1, 0, -1): #reverse count loop
        swapflag = False  

        for i in range(n):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i] # swap
                swapflag = True

        print(numbers)

        if not swapflag:
            break

print(f"List: {numbers}")
algorithm(numbers)
print(f"Sorted list: {numbers}")
