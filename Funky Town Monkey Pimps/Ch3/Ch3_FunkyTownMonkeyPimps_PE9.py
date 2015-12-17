#Name:Andrew Hunter, Greg Francis, Preston Fry, Phillip Nash
#Date:September 17, 2014
#Assignment:Ch 3 PE
#Problem:PE 9
#Purpose of the program:determine the color of the pocket indicated by a value entered by the user
#Assumptions:max value is 36 and minimum value is 0
#Other Comments:
number=int(input('Pick a number between 0 and 36'))#prompts the user to input a value
minimum=int(0)#minimum value on the roulette table
maximum=int(36)#maximum value on the roulette table
#determines if the value inputed by the user is a valid integer, if not returns an error
if int(number<minimum or number>maximum):
        print('Error')
#lists the rest of the possible valid integers and assigns a color to the value, and will return that color to the user when a value is entered        
elif number==0:
        print('Green')
elif number==1:
        print('Red')
elif number==2:
        print('Black')
elif number==3:
        print('Red')
elif number==4:
        print('Black')
elif number==5:
        print('Red')
elif number==6:
        print('Black')
elif number==7:
        print('Red')
elif number==8:
        print('Black')
elif number==9:
        print('Red')
elif number==10:
        print('Black')
elif number==11:
        print('Black')
elif number==12:
        print('Red')
elif number==13:
        print('Black')
elif number==14:
        print('Red')
elif number==15:
        print('Black')
elif number==16:
        print('Red')
elif number==17:
        print('Black')
elif number==18:
        print('Red')
elif number==19:
        print('Red')
elif number==20:
        print('Black')
elif number==21:
        print('Red')
elif number==22:
        print('Black')
elif number==23:
        print('Red')
elif number==24:
        print('Black')
elif number==25:
        print('Red')
elif number==26:
        print('Black')
elif number==27:
        print('Red')
elif number==28:
        print('Black')
elif number==29:
        print('Black')
elif number==30:
        print('Red')
elif number==31:
        print('Black')
elif number==32:
        print('Red')
elif number==33:
        print('Black')
elif number==34:
        print('Red')
elif number==35:
        print('Black')
elif number==36:
        print('Red')
