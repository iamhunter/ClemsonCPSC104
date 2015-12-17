#Name: Greg Francis, Preston Fry, Andrew Hunter, Phillip Nash
#Team Name: The Funky Town Monkey Pimps
#Assignment: CH.4 Programming Exercises
#Problem: #13
#The purpose of the program is to display a pattern using the asterisk


#This program displays a triangle pattern.
#The for statement below is the count control for the pattern with 7
#being the maximum, and 0 being the minimum within the range.
#The step value for this count controlled loop is -1 making the loop
#iterate from highest to lowest.

for star in range(7,0,-1):

#this statement takes the range and iterates the loop for
#each time there is another value that makes the range true.

    for col in range(star):
        
#the print statement below prints stars as defined in the loop above
#and the special argument "end" indicates to the program that there are
#no spaces in between the characters as they are printed.

        print('*',end='')

#this print statement identifies that the program needs to go to a new line
#before starting the next iteration of the loop.

    
    
    print()