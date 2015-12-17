#Name:Andrew Hunter, Greg Francis, Preston Fry, Phillip Nash
#Date:September 17, 2014
#Assignment:Ch 3 PE
#Problem:3
#Purpose of the program:to display whether the age of a given person is an infant, child, teenager, or adult
#Assumptions:an infant is 1 year old or less, a child is older than 1 year and less than 13 years old,
#a teenager is atleast 13 years old and less than 20 years old and an adult is greater than 20 years old
#Other Comments:nope
infant=1
child=13
teenager=19
adult=20
age=int(input('What is the persons age?'))#determines the age of the person by the user input
if age<=infant:
    print('This person is an infant.')#if the value is 1 or less the person is an infant and dislays that to the user
else:
    if age>infant and age<child:
        print('This person is a child.')#if the value entered is greater than 1 and less than 13, the person is a child, and is displayed to the user
    else:
        if age>=child and age<=teenager:
            print('This person is a teenager.')#if the value is between 13 and 19 the person is a teenager, and the user is displayed the results
        else:
            if age>=adult:
                print('This person is an adult.')#if the value is 20 or greater, the person is an adult and the user is given the information
                
        
    
