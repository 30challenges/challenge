num = int(input("Enter a number: "))

def is_prime(num1):
    for i in range(2, int(num1 ** 0.5) + 1):
        if num1 % i == 0:
            return False
    return True

if is_prime(num):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")