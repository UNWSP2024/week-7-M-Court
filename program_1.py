# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.



#1: Rainfall
#user enters the total rainfall for each of 12 months into a list
#calculate & display 
	#tot. rainfall for year
	#ave. monthly rainfall
	#the months w/ highest & lowest amounts

#create list
yearly_rain_list = []

#fine total rainfall
def make_rain_list():
	#populate list
	for months in range(1,4):
		#get 1 month's rain
		monthly_rain = int(input(f"Enter the rainfall for month {months}: "))
	#populate list
	yearly_rain_list.append(monthly_rain)
	return yearly_rain_list

#find total
def total_rain_function(yearly_rain_list):
	total_rain = sum(yearly_rain_list)
	return total_rain

#find average
def find_average(total_rain):	
	average = total_rain/12
	return average

def high(yearly_rain_list):
	highest_month = max(yearly_rain_list)
	return highest_month	
		
def low(yearly_rain_list):
	lowest_month = min(yearly_rain_list)
	return lowest_month


#PART 2 RUN FUNCTIONS----------------------------------

#make list of rain each month
make_rain_list()
#get total rain
total_rain_function(yearly_rain_list)
#find average
find_average(total_rain)
#find highest
high(yearly_rain_list)
#find lowest
low(yearly_rain_list)

#PART 3 DISPLAY-----------------------------------------

print(f"{yearly_rain_list}")
#display total
print(f"the total rainfall for the year is {total_rain}")
#display average
print(f"the average for the year is {average}")
#display highest
print(f"highest rainfall month is {highest_month} in")
#display lowest
print(f"lowest rainfall month is {lowest_month} in")
