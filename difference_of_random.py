# Activity: 4
# Take a random 2-digit number, subtract it from hundred and print its magnitude only.

from random import randint

num = randint(10,99)

sub = num - 100

print("The difference of ", num, "and 100 is ", sub)
