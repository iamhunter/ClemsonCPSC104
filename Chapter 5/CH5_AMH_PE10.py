#Name:Andrew Hunter, Greg Francis, Preston Fry
#Date:October 7, 2014
#Assignment:Ch. 4 Programming Excercise
#Problem:10

def feet_to_inches():
    feet=int(input('Enter an integer number of feet'))
    
    inches=convert(feet)

    print('There are', inches, 'inches in', feet,'feet.')
    
def convert(feet):
    return feet*12

feet_to_inches()
