"""
OrderOfNumbers
"""
no1 = int(input("Please write your 1st number >> "))
no2 = int(input("Please write your 2nd number >> "))
no3 = int(input("Please write your 3rd number >> "))

if no1 < no2 < no3:
    print("numbers are ascending")
elif no1 > no2 > no3:
    print("numbers are descending")
else:
    if no1 % 2 == 0 and no2 % 2 == 0 and no3 % 2 == 0:
        print("no specific order, but all even")
    elif no1 % 2 != 0 and no2 % 2 != 0 and no3 % 2 != 0:
        print("no specific order, but all odd")
    else:
        print("no specific order")

"""
SumUp
"""
n1 = int(input("Please write your n1 here: >> "))
n2 = int(input("Please write your n2 here: >> "))

if n1 <= 0 or n2 <= 0 or n1 <= 0 and n2 <= 0:
    print("Both n1 and n2 need to be > 0")
elif 0 < n2 < n1:
    print("n2 needs to be > n1")
else:
    while True:
        print(n1)
        n1 += 1
        if n1 > n2:
            break
