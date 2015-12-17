#Name:Andrew Hunter, Greg Francis, Preston Fry, Phillip Nash
#Date:September 17, 2014
#Assignment:Ch 3 PE
#Problem:4
#Purpose of the program:convert numbers into roman numerals
#Assumptions:program can convert numbers 1-10 into roman numerals
number1=1
number2=2
number3=3
number4=4
number5=5
number6=6
number7=7
number8=8
number9=9
number10=10
roman_numeral=int(input('What is the value you want to convert to a roman numeral?'))
#gets the value the user wants to convert to a roman numeral
if roman_numeral>number10 or roman_numeral<number1:
    print('Error')
#determines whether the entered value falls in the range accepted by the program and if it does, continues to convert into
#the value into a roman numeral, if not it will return an error message to the user                
elif roman_numeral==number1:
    print('I')
elif roman_numeral==number2:
    print('II')
elif roman_numeral==number3:
    print('III')
elif roman_numeral==number4:
    print('IV')
elif roman_numeral==number5:
    print('V')
elif roman_numeral==number6:
    print('VI')
elif roman_numeral==number7:
    print('VII')
elif roman_numeral==number8:
    print('VIII')
elif roman_numeral==number9:
    print('IX')
elif roman_numeral==number10:
    print('X')

    
                                        
        
                
