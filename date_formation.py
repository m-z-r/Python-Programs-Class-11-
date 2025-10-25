# Activity: 2
# Take three inputs: date, month, and year from the user. Print them in three formats:
# date - month - year
# month - date - year
# year - month - date

date, month, year = input("Enter date, month and year (separated by space): ").split()
# split() is used to take multi-variable input

print(date + "-" + month + "-" + year) 
print(month + "-" + date + "-" + year)
print(year + "-" + month + "-" + date)

# '+' is concatenation symbol for numbers/strings
