principal = int(input("Enter principal (inital amount in GBP): "))
interest = int(input("Enter interest rate (as percentage, without percentage sign): "))
time = int(input("Enter interest time (in years): "))

# simple formula = P(1 + it)

# convert the interest to something that we can multiply
newinterest = (interest / 100)

# math
simple = principal + (principal * newinterest * time)

print(f"After {time} years at a rate of {interest}%, you will have £{simple}.")