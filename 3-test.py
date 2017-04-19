import math

def isDivisible(x,y):
    if x % y == 0:
        result = True            #checks if two numbers are divisible
    else:
        result = False
    return result



def Sum_Of_Divisors(x):
    total = 1
    i = 2
    bound = x//2
    while (i <= bound):           
        if isDivisible(x,i):              
            total = total + i
        i = i + 1
    return total

print(Sum_Of_Divisors(28))
