#Name:Andrew Hunter, Greg Francis, Preston Fry
#Date:October 7, 2014
#Assignment:Ch. 5 Programming Excercise
#Problem: 12

def max():
    first=int(input('Enter your first integer'))
    second=int(input('Enter your second integer'))

    big=large(first,second)

    print('The largest of your two integers is', big)
def large(one,two):
    if one>two:
        return one
    elif one<two:
        return two
    else:
        return 'neither because your numbers are the same. Duh'
    
max()
