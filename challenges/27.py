principal = int(input("Enter principal (inital amount in GBP): "))
interest = int(input("Enter interest rate (as percentage, without percentage sign): "))
time = int(input("Enter interest time (in years): "))

def compound_interest(principal, interest, time):

    # Calculates compound interest
    investment = principal * (pow((1 + interest / 100), time))
    compound = investment - principal
    print(f"After {time} years at a rate of {interest}%, you will have £{compound}.")

compound_interest(principal, interest, time)