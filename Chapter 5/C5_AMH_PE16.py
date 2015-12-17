#Name:Andrew Hunter
#Date:October 2014
#Assignment:Ch. 5 Programming Excercise
#Problem: 16
import random
number = 0
odd = 0
even = 0

while number < 100:
    random.randint(1,1000)
    number = number + 1
    if random.randint(1,1000)%2==0:
        even = even + 1
    else:
        odd = odd + 1

print (even,'numbers were even and',odd,'were odd')
