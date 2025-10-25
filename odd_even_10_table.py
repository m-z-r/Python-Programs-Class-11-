def even_numbers(even_num):
    for i in range (1,11,2):
        print("\n")
        sum_even = even_num + i
        for j in range (1,11,1):
            prod_even = sum_even * j
            print("",sum_even,"x ",j,"= ",prod_even)



def odd_numbers(odd_num):
    for x in range (1,11,2):
        print("\n")
        sum_odd= odd_num + x
        for y in range (1,9,1):
            prod_odd = sum_odd * y
            print("",sum_odd,"x ",y,"= ",prod_odd)

print(odd_numbers(1))
print(even_numbers(2))
