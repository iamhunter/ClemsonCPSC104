#Name:Andrew Hunter, Greg Francis, Preston Fry, Phillip Nash
#Date:October 7, 2014
#Assignment:Ch. 4 Programming Excercises
#Problem: 2
#Purpose of the program: Displays Calories burned
#Assumptions: You burn 4.2 calories per minute

#prints a header for the table
print("Minutes\tCalories")
print("-------------------")

#loop that calculates caleries burned after a given time period and
#then prints that amount
for number in range(10,31,5):
    calories= number*4.2
    print(number, "\t", calories)
    


