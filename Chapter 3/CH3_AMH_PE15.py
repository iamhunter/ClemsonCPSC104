#Name:Andrew Hunter
#Date:September 17, 2014
#Assignment:Ch 3 PE
#Problem:15
#Purpose of the program:Display minutes, hours, days and seconds from seconds
#Assumptions:
#Other Comments:
seconds=int(input('Enter a number of seconds'))
minutes=int(seconds/60)
hours=int(minutes/60)
days=int(hours/24)
secondminutes=seconds-(minutes*60)
minutehours=minutes-(hours*60)
hourdays=hours-(days*24)
if 0<=seconds<60:
        print(seconds,
              'seconds')
elif 0<=seconds<3600:
        print(minutes,
              'minutes and',
              secondminutes,
              'seconds.')
elif 0<=seconds<86400:
        print(hours,
              'hours,',
              minutehours,
              'minutes and',
              secondminutes,
              'seconds.')
elif 0<=seconds>=86400:
        print(days,
              'days,',
              hourdays,
              'hours,',
              minutehours,
              'minutes and',
              secondminutes,
              'seconds.')
else:
        print('Error')
