#Name:Andrew Hunter
#Date:September 17, 2014
#Assignment:Ch 3 PE
#Problem:6
#Purpose of the program:Determine whether or not a date is magic
#Assumptions:
#Other Comments:
month=int(input('Enter a numerical month'))
day=int(input('Enter a numerical day'))
year=int(input('Enter the last two digits of a year'))
if 0<month<12:
        if 0<day<31:
                if 0<year:
                        if year==day*month:
                                print('This date is magic')
                        else:
                                print('This date is not magic')

