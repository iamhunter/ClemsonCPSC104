#Name:Andrew Hunter, Greg Francis, Preston Fry
#Date:October 7, 2014
#Assignment:Ch. 5 Programming Excercise
#Problem: 17 

def main():
    number=int(input('Enter a number'))
    prime=is_prime(number)

    print('Your number',prime,'prime')
def is_prime(one):
    for i in range(2, one):
        if n % i == 0:
            return 'is not'
    return 'is'
main()
