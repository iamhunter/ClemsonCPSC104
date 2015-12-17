#Name:Andrew Hunter, Greg Francis, Preston Fry, Phillip Nash
#Date:October 7, 2014
#Assignment:Ch. 4 Programming Excercises
#Problem: 12
#Purpose of the program: Displays organism population

start=int(input('Starting number of organisms:'))
increase=float(input('Enter the average daily percent increase as a decimal:'))
days=int(input('Number of days to multiply:'))
print('Day\tApporoximate Population')
for number in range(days):

#uses the population growth formula to calculate values and display
#in a table based on the values entered by the user.
    print(number+1,'\t',(start*((1+increase)**number)))
