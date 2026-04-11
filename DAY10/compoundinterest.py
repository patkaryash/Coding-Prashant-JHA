#WAP to calculate the compound interest for a principal amount , rate and  time
p = int(input("Enter the principal amount: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time in years: "))
c = p * (1 + r/100)**t - p
print("Compound Interest = ", c)