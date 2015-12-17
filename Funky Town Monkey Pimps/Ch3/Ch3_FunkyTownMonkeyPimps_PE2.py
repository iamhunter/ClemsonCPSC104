#Name:Andrew Hunter
#Date:September 17, 2014
#Assignment:Ch 3 PE
#Problem:2
#Purpose of the program:Find the larger area
#Assumptions:
#Other Comments:
length1=int(input('What is the length of rectangle 1'))
width1=int(input('What is the width of rectangle 1'))
length2=int(input('What is the length of rectangle 2'))
width2=int(input('What is the width of rectangle 2'))
area1=length1*width1
area2=length2*width2
print('The area of the first rectangle is',
      area1)
print('The area of the second rectangle is',
      area2)
if area1>area2:
        print('Therefore, the first rectangle has a larger area.')
elif area1<area2:
        print('Therefore, the second rectangle has a larger area.')
elif area1==area2:
        print('Therefore, the two rectangles have the same area.')
