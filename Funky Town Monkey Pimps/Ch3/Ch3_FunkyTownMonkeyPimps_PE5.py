#Name:Andrew Hunter
#Date:September 17, 2014
#Assignment:Ch 3 PE
#Problem:5
#Purpose of the program:Determine whether or not an object is too heavy or light
#Assumptions:
#Other Comments:
mass=int(input("What is the object's mass in kg?"))
weight=mass*9.8
print("The object's weight is",
      int(weight),
      'newtons')
if weight>500:
        print('The object is too heavy')
if weight<100:
        print('The object is too light')
