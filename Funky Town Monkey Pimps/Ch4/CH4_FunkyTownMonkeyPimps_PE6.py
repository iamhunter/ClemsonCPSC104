#Name: Greg Francis, Preston Fry, Andrew Hunter, Phillip Nash
#Team Name: The Funky Town Monkey Pimps
#Assignment: CH.4 Programming Exercises
#Problem: #6
#purpose:to display the fahrenheit conversions of celsius temperatures zero through 20
#assumptions: the formula for converting temperatures to fahrenheit is
# (9/5)C +32

print('Celsius\tFahrenheit')
print('-------------------')
for celsius in range(0,21,1):
    fah=(((9/5)*celsius)+32)
    print (celsius,'\t',fah)    
