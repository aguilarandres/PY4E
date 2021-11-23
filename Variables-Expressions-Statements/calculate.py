"""
Program that prompts the user for hours and rate per hour to compute gorss pay
"""

# store user input for hours
hours = float( input("Enter Hours: ") )

# store user input for rate
rate = float( input("Enter Rate: " ) )

# calculate gross pay
gross_pay = hours * rate

# display gross pay on screen
print("Pay:", gross_pay)
