#Name:Andrew Hunter, Greg Francis, Preston Fry
#Date:September 18, 2014
#Assignment:Ch. 3 Programming Excercises
#Problem: 12
#Purpose of the program:display the discount on a given purchase and then the
#total price after the discount
#Assumptions: 10-19 packages purchased earns a 10% discount
#20-49 packages purchased earns a 20% discount
#50-99 packages purchased earns a 30% discount
#100 or more packages purchased earns a 40% discount
software=99#the price of a single software package
discount1=.1#discount for the purchase of 10-19 packages
discount2=.2#discount for the purchase of 20-49 packages
discount3=.3#discount for the purchase of 50-99 packages
discount4=.4#discount for the purchase of 100 or more packages
quantity=float(input('How many software packages would you like to purchase?'))#prompts the user to enter the number of packages desired
purchase_price=quantity*software#calcuates the purchase price of the inputed number of software packages
if quantity>=10 and quantity<=19:#desides how many packages are needed, the discount applied and then displays total price after discount and the discount
    print('Your software package will cost $',format(purchase_price-purchase_price*discount1,',.2f'),\
          ' and the discount you received is $',format(purchase_price*discount1,',.2f'),sep='')
elif quantity>=20 and quantity<=49:
    print('Your software package will cost $',format(purchase_price-purchase_price*discount2,',.2f'),\
          ' and the discount you received is $',format(purchase_price*discount2,',.2f'),sep='')
elif quantity>=50 and quantity<=99:
    print('Your software package will cost $',format(purchase_price-purchase_price*discount3,',.2f'),\
          ' and the discount you received is $',format(purchase_price*discount3,',.2f'),sep='')
elif quantity>=100:
    print('Your software package will cost $',format(purchase_price-purchase_price*discount4,',.2f'),\
          ' and the discount you received is $', format(purchase_price*discount4,',.2f'),sep='')
else:
    print('Your software package will cost$',format(purchase_price,',.2f'),' and you did not receive a discount today',sep='')
    
    
    
    
               
