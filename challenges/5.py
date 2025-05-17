num = int(input("Enter a number: "))
iterations = int(input("How many iterations? "))

for iterations in range(1, iterations+1):
    print(num, 'x', iterations, '=', num*iterations)