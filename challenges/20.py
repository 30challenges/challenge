terms = int(input("How many terms? "))
num1 = 0
num2 = 1
flag = 0

while flag < terms:
    print(num1)
    nthterm = num1 + num2
    num1 = num2
    num2 = nthterm
    flag += 1