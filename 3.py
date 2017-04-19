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
    bound = x/2
    while (i <= bound):            #checking the numbers smaller than chosen integer
        if isDivisible(x,i):              
            total = total + i
        i = i + 1
    return total

def Sequence():
    n1 = 1                        #setting the first number of the sequence
    finish = False
    while (finish == False and n1 <= 20000): 
        n2 = Sum_Of_Divisors(n1)
        n3 = Sum_Of_Divisors(n2)
        n4 = Sum_Of_Divisors(n3)
        n5 = Sum_Of_Divisors(n4)
        if n1 == Sum_Of_Divisors(n5) and n1 != n2 and n2 != n3 and n4 != n5 and n5 != n1:  #making sure no two numbers in the sequence are the same
            finish = True
        else:
            n1 = n1 + 1
    return n1, n2, n3, n4, n5

print(Sequence())


            
        







    
