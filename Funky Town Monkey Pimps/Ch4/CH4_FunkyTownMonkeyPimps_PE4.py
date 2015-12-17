#Name:Andrew Hunter, Greg Francis, Preston Fry, Phillip Nash
#Date:October 8, 2014
#Assignment:Ch. 4 Programming Excercises
#Problem: 4
#Purpose of the program: Find the distance traveled

#Get inputs for speed and hours traveled
speed=int(input('What is the speed of the vehicle in mph? '))
hours=int(input('How many hours did it travel? '))
print('Hour\tDistance Traveled')

#Multiply Speed by Hours to get Distance Traveled
for number in range(1,hours+1):
    print(number, '\t', (speed*number))
    
    
