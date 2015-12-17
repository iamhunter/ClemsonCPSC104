#Name:Andrew Hunter, Greg Francis, Preston Fry
#Team Name:Funky Town Monkey Pimps
#Date:September 2, 2014
#Assignment:Ch. 2 Programming Excercises
#Problem: 6
#Purpose of the program:Calculate tax and total price of any given item
#Assumptions:state and county tax
#Other Comments:
item=float(input('How much did your item cost?'))
state_tax=item*float(.05)
county_tax=item*float(.025)
print ('Your state tax is $',
       format(state_tax,'.2f'),
       sep='')
print ('Your county tax is $',
       format(county_tax,'.2f'),
       sep='')
total_tax=state_tax+county_tax
print ('Your total tax is $',
       format(total_tax,'.2f'),
       sep='')
total=state_tax+county_tax+item
print ('Your total is $',
       format(total,'.2f'),
       sep='')

