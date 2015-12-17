#Name:Andrew Hunter, Greg Francis, Preston Fry
#Team Name:Funky Town Monkey Pimps
#Date:September 2, 2014
#Assignment:Ch. 2 Programming Excercises
#Problem: 2
#Purpose of the program:Display profit from total sales.
#Assumptions:Profit is 23% of total sales
#Other Comments:
total_sales=float(input('What are the total sales?'))
profit=total_sales*.23
print('Given that your total sales are $',
      format(total_sales, '.2f'),
      sep='',)
print(', your profit is $',
      format(profit, '.2f'),
      sep='')
