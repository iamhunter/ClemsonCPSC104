#Name:Andrew Hunter, Greg Francis, Preston Fry, Phillip Nash
#Date:October 8, 2014
#Assignment:Ch. 4 Programming Excercises
#Problem: 11
#Purpose of the program: Calculate the Factoral of a number

#Set accumulator to 1
start=1

#Have user input a number
base=int(input('What do you want to find the factorial of?'))

#Make sure number is positive
if base<0:
    print('Sorry the factorial of a negative number does not exsist.')
elif base==0:
    print('The factorial of 0 is 1.')
else:

#Find factoral of the input    
    for r in range (1,base+1):
        start=(start*r)
    print('The factorial of',base,'is',start,'.')
    
