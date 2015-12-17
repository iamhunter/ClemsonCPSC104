#Name:Andrew Hunter, Greg Francis, Preston Fry
#Date:September 18, 2014
#Assignment:Ch. 3 Programming Excercises
#Problem: 13
#Purpose of the program:calculate the shipping charges of a package based on weight.
#Assumptions: rate per pound is $1.50 if 2 pounds or less
#$3.00 per pound if over 2 pounds but less than or equal to 6 pounds
#$4.00 per pound if over 6 pounds but less than or equal to 10 pounds
#$4.75 per pound if over 10 pounds
pounds=float(input('How much does your package weigh?'))#prompts the user to input a weight for the package
if pounds<=2:#uses the weight entered to calculate a cost of shipping the package based on the decision structure below
    print('The cost of shipping your package is $',format(pounds*1.5,',.2f'), sep='')
elif pounds>2 and pounds<=6:
    print('The cost of shipping your package is $',format(pounds*3.0,',.2f'), sep='')
elif pounds>6 and pounds<=10:
    print('The cost of shipping your package is $',format(pounds*4.0,',.2f'), sep='')
elif pounds>10:
    print('The cost of shipping your package is $',format(pounds*4.75,',.2f'), sep='')
    
