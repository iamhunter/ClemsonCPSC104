#Name:Andrew Hunter, Greg Francis, Preston Fry
#Date:October 7, 2014
#Assignment:Ch. 5 Programming Excercise
#Problem: 4

def main():
    loan=int(input('How much is your monthly loan payment?'))
    insurance=int(input('How much is your monthly insurance payment?'))
    gas=int(input('How much do you pay monthly for Gas?'))
    oil=int(input('How much do you pay monthly for oil?'))
    tires=int(input('How much do you pay monthly for tires?'))
    maintenance=int(input('How much do you pay monthly for maintenance?'))
    
    total = add(loan,insurance,gas,oil,tires,maintenance)
    annual=sum_annual(total)
    
    print('Your monthly loan payment is', loan)
    print('Your monthly insurance payment is', insurance)
    print('Your monthly gas payment is', gas)
    print('Your monthly oil payment is', oil)
    print('Your monthly tire payment is', tires)
    print('Your monthly maintenance payment is', maintenance)
    print('Your total monthly payment is', total)
    print('Your total annual payment is', annual)


def add(num1, num2, num3, num4, num5, num6):
    sum=(num1 + num2 + num3 + num4 + num5 + num6)
    return sum

def sum_annual(yes):
    result=yes*12
    return result

main()
