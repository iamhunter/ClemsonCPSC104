#Name:Andrew Hunter, Greg Francis, Preston Fry
#Date:September 2, 2014
#Assignment:Ch. 2 Programming Excercises
#Problem: 11
#Purpose of the program:Display percentages of males and females in a class.
#Assumptions:There are males and females in the class
#Other Comments:
males=int(input('How many males are in the class?'))
females=int(input('How many females are in the class?'))
total=males+females
percentm=(males/total)
percentf=(females/total)
print('The percentage of males in the class is',
      format(percentm, '.2f'))
print('The percentage of females in the class is',
      format(percentf, '.2f'))
