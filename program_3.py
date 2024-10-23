#Have the user input (using a loop) various information that contains three pieces of data: year, name of state, and population.  Store all of this information in a list of lists.  For example it might be stored like this:

#[[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]

#Now have the user enter a year.  The program will add the populations from all states in the list of list for that year only

repeat = "y"
all_entered_values = []

def main():
	while True:
		#populate list
		year = int(input("Enter the year: "))
		name = input("Enter the state's name: ")
		population = int(input("Enter the population: "))

		#create tuple
		state_tuple = ()
		#populate tuple
		state_tuple = (year, name, population)
		#populate total list
		all_entered_values.append(state_tuple)

		#repeat?
		repeat = input("Do you have another entry? Enter 'y' for yes.")
		#repeat
		if repeat == "y":
			print("Create another entry...")
		#not repeat
		if repeat != "y":
			print(all_entered_values)
			#return list and total
			return all_entered_values

def sum_population(user_year, all_entered_values):
	#declare
	total_population = 0
	#get year
	
	print(all_entered_values)
	#add to total_population
	for state_list in all_entered_values:
		if state_list[0] == user_year:
			total_population += state_list[2]
	return total_population

#populate tuples and list
all_populated_lists = main()
print(all_populated_lists)

#find sum
user_year = int(input("What year? "))
total_population = sum_population(user_year, all_populated_lists)
print(f"the total population in {user_year} was {total_population}")
