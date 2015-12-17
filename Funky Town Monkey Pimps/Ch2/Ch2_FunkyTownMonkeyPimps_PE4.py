#Name:Andrew Hunter, Greg Francis, Preston Fry
#Team name:Funky Town Monkey Pimps
#Date:September 2, 2014
#Assignment:Ch. 2 Programming Excercises
#Problem: 4
#Purpose of the program:Display subtota, tax, and total
#Assumptions:Tax is 7%
#Other Comments:
item_1=float(input('How much did item 1 cost?'))
item_2=float(input('How much did item 2 cost?'))
item_3=float(input('How much did item 3 cost?'))
item_4=float(input('How much did item 4 cost?'))
item_5=float(input('How much did item 5 cost?'))
subtotal=item_1+item_2+item_3+item_4+item_5
print ('Your subtotal is $',
       format(subtotal,'.2f'),
       sep='')
tax=subtotal*float(.07)
print ('Your tax is $',
       format(tax,'.2f'),
       sep='')
total=subtotal+tax
print ('Your total is $',
       format(total,'.2f'),
       sep='')
