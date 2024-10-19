# Program #3: US_Population
#def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
 #   all_entered_values = []

    # Now have the user enter a year. 
    
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

# def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.

    # print the totalled population


# Call the main function.
#if __name__ == '__main__':
 #   main()

    
#-------------MY CODE-------------#    

repeat = "y"
all_entered_values = []

def main():
	while True:
		#populate list
		year = int(input("Enter the year: "))
		name = input("Enter the state's name: ")
		population = int(input("Enter the population: "))
		
		#create tuple
		list = ()
		#populate tuple
		list = (year, name, population)
		#populate umbrella list
		all_entered_values.append(list)
		return list
		return all_entered_values
		
		repeat = input("Do you have another entry? Enter 'y' for yes.")
		#repeat
		if repeat == "y":
			print("Create another entry...")
		#not repeat
		if repeat != "y":
			print(all_entered_values)
			break

def sum_population(list, all_entered_values):
	#get year
	user_year = int(input("What year? "))
	while user_year in list:
		total_population += list(2)
		print(total_population)

#populate tuples and list
main()
#find sum
total_population = sum_population(list,all_entered_values)
print(total_population)
