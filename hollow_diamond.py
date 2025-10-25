# Activity:3
# Take input from the user, which determines the height of a hollow diamond, and print it

height = int(input("Enter the height of the diamond: "))

#loop for space in b/w triangles
for i in range(1, height + 1):
    print(" " * (height - i), end="")
    if i == 1:                         # upper triangle in diamond
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")

for i in range(height - 1, 0, -1):
    print(" " * (height - i), end="")
    if i == 1:                         # lower triangle in diamond
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")
