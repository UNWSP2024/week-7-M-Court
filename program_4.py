# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 

#import
import math

#find distance
def distance_function(point1, point2):
	#define coordinates 
	x1 = point1[0]
	y1 = point1[1]
	z1 = point1[2]
	x2 = point2[0]
	y2 = point2[1]
	z2 = point2[2]
	#calculate distance
	distance = math.sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)
	return distance
	
#get two points
def main():
	try:
		print("enter 1st point...")
		#populate tuple 1
		x1 = int(input("enter x1: ")) 
		y1 = int(input("enter y1: "))
		z1 = int(input("enter z1: "))
		#create tuple 1
		point1 = (x1, y1, z1)
	
		#populate tuple 2
		print("enter 2nd point...")
		x2 = int(input("enter x2: ")) 
		y2 = int(input("enter y2: "))
		z2 = int(input("enter z2: "))
		#create tuple 2
		point2 = (x2, y2, z2)
	
		#if input is faulty
	except:
			print("Faulty input. Input must be an integer.")
	
	print(f"the distance between those points is {distance_function(point1, point2)}")

main()

#thank you for all your help!