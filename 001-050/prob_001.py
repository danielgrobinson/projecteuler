#!/usr/bin/python3
# Multiples of 3 and 5
# Problem 1￼
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

def sumof(nn):
    """
    sum values from 1 to nn
    """
    sum = 0
    while nn > 0:
        sum = sum + nn
        nn -= 1

    return sum

sum3 = sumof((1000-1)//3)
sum5 = sumof((1000-1)//5)
sum15 = sumof((1000-1)//15)

print("sum :", (3*sum3) + (5 * sum5) - (sum15 * 15))
