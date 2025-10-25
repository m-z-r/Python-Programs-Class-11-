num = int(input("Enter any number to print its table: "))

def table(num):
    for i in range (1,11):
        prod = num * i
        print("",num,"x",i,"=",prod)

table(num)
