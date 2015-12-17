#Name:Andrew Hunter
#Date:September 2, 2014
#Assignment:Ch. 2 Programming Excercises
#Problem: 12
#Purpose of the program:Find Out Stock Information
#Assumptions:Joe isn't lying
#Other Comments:
shares=2000
ppps=40.00
comish=.03
spps=42.75
totalb=ppps*shares
comishb=totalb*comish
totals=spps*shares
comishs=totals*comish
total=totals-(totalb+comishb+comishs)
print('When purchasing his stock, Joe paid $',
      format(totalb, '.2f'),
      sep='')
print('When purchasing his stock, Joe paid his broker $',
      format(comishb, '.2f'),
      sep='')
print('When selling his stock, Joe recieved $',
      format(totals, '.2f'),
      sep='')
print('When selling his stock, Joe paid his broker $',
      format(comishs, '.2f'),
      sep='')
print("In total, Joe's net profit was $",
      format(total, '.2f'),
      sep='')
      
