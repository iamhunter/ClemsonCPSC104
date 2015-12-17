#Name:Andrew Hunter, Greg Francis, Preston Fry
#Date:October 7, 2014
#Assignment:Ch. 5 Programming Excercise
#Problem: 8

def main():
    space=int(input('How many square feet of wall space need painting?'))
    price=int(input('How much does the paint cost per gallon?'))

    gallons=amount(space)
    labor=work(space)
    cost_paint=cost(price, gallons)
    labor_cost=labor_cost1(labor)
    total_cost=total(cost_paint, labor_cost)
    
    print('The amount of gallons that you will need is',format(gallons, '.2f'))
    print('The amount of labor that you will need is',labor)
    print('The cost of paint for your job is',format(cost_paint, '.2f'))
    print('The cost of labor for your job is',format(labor_cost, '.2f'))
    print('The total cost of your job is',format(total_cost, '.2f'))
    
def amount(sqfeet):
    return float(sqfeet/112)

def work(sqfeet):
    return int((sqfeet/112)*8)

def cost(one, two):
    return (one*two)

def labor_cost1(one):
    return one*35

def total(one, two):
    return (one+two)

main()
