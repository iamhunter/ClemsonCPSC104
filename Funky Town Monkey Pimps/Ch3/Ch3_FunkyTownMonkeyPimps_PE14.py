#Name:Andrew Hunter, Greg Francis, Preston Fry
#Date:September 18, 2014
#Assignment:Ch. 3 Programming Excercises
#Problem: 14
#Purpose of the program:to calculate a persons body mass index(BMI)
#Assumptions:BMI = weight * 703//height**2
#Other Comments:optimal bmi is between 18.5 and 25
#if bmi is under 18.5 the person is considered to be underweight
#and over 25 considered overweight
weight=float(input('What is your weight in pounds?'))
height=float(input('What is your height in inches?'))
bmi=weight*703//height**2
if bmi>=18.5 and bmi<=25:
    print('Your BMI is',bmi,'and is optimal for your weight and height.')
elif bmi>25:
    print('Your BMI is',bmi,'and you are overweight for your height.')
elif bmi<18.5:
    print('Your BMI is',bmi,'and you are underweight for your height.')
