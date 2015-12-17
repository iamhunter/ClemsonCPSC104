#Name:Andrew Hunter, Greg Francis, Preston Fry
#Date:September 18, 2014
#Assignment:Ch. 3 Programming Excercises
#Problem: 11
#Purpose of the program:display the points earned for the number of books
#purchased by the customer
#Assumptions:if the customer doesn't purchase any books, they don't get any points
#if they purchase 2 books they earn 5 points, if they purchase 4 books
#they earn 15 points, if they purchase 6 books they earn 30 points, and
#if they purchase 8 or more books they earn 60 points
books=int(input('How many books did you purchase?'))#asks the user how many books they purchased and sets variable books to the value
if books==2: #the elif statement determines how many books were purchased and displays the amount of points earned
    print('Your purchase has earned you 5 points!')
elif books==4:
    print('Your purchase has earned you 15 points!')
elif books==6:
    print('Your purchase has earned you 30 points!')
elif books>=8:
    print('Your purchase has earned you 60 points!')
else:
    print('Your purchase did not earn any points today!')
    
