#Name:Andrew Hunter, Greg Francis, Preston Fry, Phillip Nash
#Date:October 7, 2014
#Assignment:Ch. 4 Programming Excercises
#Problem: 3
#Purpose: To calculate the user's expenses for the month
#and display whether they're over or under budget

#Set accumulator to 0
total=0

#set keep_going equal to y
keep_going='y'

#Have user input monthly budget
budget=float(input('Enter your desired monthly budget: '))

#Get user's monthly bill inputs and add to total
while keep_going=='y':
    bills=float(input('Enter a bill: '))
    total=total+bills

#Ask user is they have any more bills to input
    keep_going=input('Do you want to add another bill? Type y for yes: ')

#Print the amount under budget
if total>budget:
    print('You are over budget by', total-budget, 'dollars')

#Print amount over budget
else:
    print('You are under your budget by', budget-total, 'dollars')
             
