# Generate list of even numbers from 1 to 100
even = []
for num in range(1, 101):
    if num % 2 == 0:
        even.append(num)
print(even)