#Name:Andrew Hunter, Greg Francis, Preston Fry
#Date:October 7, 2014
#Assignment:Ch. 5 Programming Excercise
#Problem: 21
import random
def main():
    computernumber=random.randint(1,3)
    humanword=input('rock, paper, or scissors')
    humannumber=from_word(humanword)
    computerword=from_number(computernumber)
    decision=winner(computernumber,humannumber)

    print('You have chosen',humanword,
          'and the computer has chosen',computerword,
          'Therefore',decision)
    
def from_word(one):
    if one=='rock':
        return 1
    elif one=='paper':
        return 2
    elif one=='scissors':
        return 3

def from_number(one):
    if one==1:
        return 'rock'
    elif one==2:
        return 'paper'
    elif one==3:
        return 'scissors'
    
def winner(one,two):
    difference=one-two
    if difference%3==1:
        return 'the computer wins'
    elif difference%3==2:
        return 'you win!'
    elif difference==0:
        return 'you have tied with the computer. Please run the program again.'
    elif difference==0:
        return restart()

def restart():
    main()
main()
