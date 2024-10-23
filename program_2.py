#2: Larger than n

#In a program, write a function (with NO output) that accepts two arguments: 
		#a list
		#and a number n.  
#Assume that the list contains numbers. The function should display all of the numbers in the list that are greater than the number n.


#STARTER DEFINITIONS
#define "repeat"
repeat = "y"
#list for greater
GREATER = []
#list for less
LESSER = []

def display_greaters(number):
	while True:
		#populate numbers
		if number > n:
			GREATER.append(number)
		if number <= n:
			LESSER.append(number)
			
		#repeat?
		repeat = input("would you like to enter another number? If so, type 'y'.")	
		#repeat		
		if repeat == "y":
				number = int(input("enter a number: "))
		#not repeat
		if repeat != "y":
			break		

#user defines n
n = int(input("Enter a number for 'n': "))
#user enters 1st number
number = int(input("enter a number: "))	
#user creates list with function
display_greaters(number)
#print
print(f"The numbers greater than 'n' are {GREATER}")	
