#Name: Phillip Nash, Andrew Hunter, Preston Fry, Gregory Francis
#Date: October 6,2014
#Assignment: Chapter 4
#Problem: PE 8
#Purpose of the program: Sum of Numbers
total=0.0# accumulator
number=float(input("enter a positive number"))# user input
while number>0:# while statement
    number=float(input("enter a positive number"))
    total=number+total
if number<0:# loop false statement
    print("the total is:", total)
