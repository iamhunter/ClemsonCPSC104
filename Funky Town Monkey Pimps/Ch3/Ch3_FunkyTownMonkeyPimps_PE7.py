#Name:Andrew Hunter, Greg Francis, Preston Fry
#Date:September 18, 2014
#Assignment:Ch. 3 Programming Excercises
#Problem: 7
#Purpose of the program:to display a secondary color for the user, given two primary colors
#Assumptions:red and blue make purple, red and yellow make orange, blue and yellow make green
#Other Comments:this was really hard to figure out ...
red=1#assigns an integer value to each color
blue=2
yellow=3
print('Mixing two primary colors will create one',#explains how to use the program to the user
      'of the secondary colors.',\
      'Enter 1 for red, enter 2 for blue and enter 3 for yellow.')
color1=int(input('Enter the first primary color you want to mix:'))#prompts the user for a color
color2=int(input('Enter the second primary color you want to mix:'))#prompts the user for the second color 
if color1+color2==3:#displays the color created by the user
    print('The secondary color you created is purple.')
elif color1+color2==4:
    print('The secondary color you created is orange.')
elif color1+color2==5:
    print('The secondary color you created is green.')
else:#displays an error if invalid colors are combined, or in this case integers that are not associated with a color.
    print('You did not create a secondary color!')
          
    

