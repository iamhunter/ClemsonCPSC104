#Name:Andrew Hunter, Greg Francis, Preston Fry
#Team Name: Funky Town Monkey Pimps
#Date:September 2, 2014
#Assignment:Ch. 2 Programming Excercises
#Problem:8
#Purpose of the program:Calculate tax and total
#Assumptions:Tax is 7%
#Other Comments:
food=float(input('How much did your food cost?'))
tax=food*float(.07)
tip=food*float(.18)
total=food+tax+tip
print('Your tax is $',
      format(tax, '.2f'),
      sep='')
print('If you are not scum, you should tip $',
      format(tip, '.2f'),
      sep='')
print('Your total is $',
      format(total, '.2f'),
      sep='')
