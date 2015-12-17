#Name:Andrew Hunter, Greg Francis, Preston Fry
#Date:September 18, 2014
#Assignment:Ch. 3 Programming Excercises
#Problem: 10
#Purpose of the program:to create a change counting game where the user inputs the number of pennies, nickles
#dimes and quarters, and if the amounts entered total one dollar it congratulates them, otherwise it displays the amount over
#or less than one dollar
print('Welcome to the dollar game! The goal is to create a dollar from the next series of questions. Ready? GO!')
pennies=int(input('How many pennies would you like?'))#asks the user for the amount of pennies
nickles=int(input('How many nickles would you like?'))#asks the user for the amount of nickles
dimes=int(input('How many dimes would you like?'))#asks the user for the amount of dimes
quarters=int(input('How many quarters would you like?'))#asks the user for the amount of quarters
if quarters*25+dimes*10+nickles*5+pennies*1==100:#calculates the amount inputed by the user and if it equals 100 cents it congratulates them
    print('Congratulations, You WIN!!!')
elif quarters*25+dimes*10+nickles*5+pennies*1>=100:#if the amount entered by the user is greater than 100 cents then it returns how much they went over by
    print('Sorry you were over by',quarters*25+dimes*10+nickles*5+pennies*1-100,'cents!')
else:#if the value entered by the user was less than 100 cents then it returns how much they were short of a dollar
    print('Sorry you were short by',abs(quarters*25+dimes*10+nickles*5+pennies*1-100),'cents!')
    
             
