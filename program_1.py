#1: Rainfall
#user enters the total rainfall for each of 12 months into a list
#calculate & display 
	#tot. rainfall for year
	#ave. monthly rainfall
	#the months w/ highest & lowest amounts

#create list
yearly_rain_list = []

#find total rainfall
def make_rain_list():
	#populate list
	for months in range(1,13):
		#get 1 month's rain
		monthly_rain = int(input(f"Enter the rainfall for month {months}: "))
		#populate list
		yearly_rain_list.append(monthly_rain)
	return yearly_rain_list

#find total
def total_rain_function(yearly_rain_list):
	total_rain_results = sum(yearly_rain_list)
	return total_rain_results

#find average
def find_average(total_rain_results):	
	average = total_rain_results/12
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
total_rain_results = total_rain_function(yearly_rain_list)
#find average
average = find_average(total_rain_results)
#find highest
highest_month = high(yearly_rain_list)
#find lowest
lowest_month = low(yearly_rain_list)

#PART 3 DISPLAY-----------------------------------------

print(f"In summary... {yearly_rain_list}")
#display total
print(f"Total rainfall is {total_rain_results} inches")
#display average
print(f"Average rainfall is {average: .2f} inches")
#display highest
print(f"Highest rainfall month is {highest_month} inches")
#display lowest
print(f"Lowest rainfall month is {lowest_month} inches")