while True:

 alpha = input("Enter a character to check if it is a lower or upper case letter: ")

 upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

 if alpha in upper:
    print("It is an upper-case letter.")
 elif alpha in lower:
    print("It is a lower-case letter.")
 else:
    print("It is an invalid character.")
    break
# Output
# Enter a character to check if it is a lower or upper case letter: A
# It is an upper-case letter.
# Enter a character to check if it is a lower or upper case letter: b
# It is a lower-case letter.
# Enter a character to check if it is a lower or upper case letter: @
# It is an invalid character.
