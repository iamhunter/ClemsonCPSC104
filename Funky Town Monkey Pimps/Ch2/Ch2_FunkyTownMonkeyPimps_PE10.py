#Name:Andrew Hunter, Greg Francis, Preston Fry
#Team Name: The Funky Town Monkey Pimps
#Date:September 2, 2014
#Assignment:Ch. 2 Programming Excercises
#Problem:10
#Purpose of the program:To find amount of ingredients needed
#Assumptions:The recipe is correct
#Other Comments:
cookies=int(input('How many cookies do you wish to bake?'))
sugar=1.5/48*cookies
butter=1/48*cookies
flour=2.75/48*cookies
print('You will need',
      format(sugar, '.2f'))
print('cups of sugar,',
      format(butter, '.2f'))
print('cups of butter, and',
      format(flour, '.2f'))
print('cups of flour.')
