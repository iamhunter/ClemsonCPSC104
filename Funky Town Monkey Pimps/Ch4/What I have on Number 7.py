#Name:Andrew Hunter, Greg Francis, Preston Fry
#Date:October 7, 2014
#Assignment:Ch. 4 Programming Excercises
#Problem: 10
#Purpose of the program:Project College Tuition
days=int(input('How many days?'))
for pennies in range(days):
    pennies*=2
    print('Today, the salary was', format(pennies/100, '.2f'),'dollars')
for pennies in range(days):
    pennies+=pennies
print('In total, the monay made was', format(pennies/100,'.2f'), 'dollars')
