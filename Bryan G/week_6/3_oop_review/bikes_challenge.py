# You are starting a bike-sharing service. Your first bike station will be at 14th St and 5 Ave.
# The dictionary below represents your first station.

station = { 
	'name': 'Station A',
 	'address': '14th St and 5 Ave',
 	'bikes': []
}

print('Question 1 - COMPLETED')

# You don't have any bikes at this station. Create a function 'add' that adds bikes to the bikes list.
# A bike can be represented by an id number in the bikes list
# Parameters: id (int)
# Returns: nothing
def add_a_bike(id):
	station['bikes'].append(id)

print('')

print('Question 2 - COMPLETED')
# Create a function 'check_out' to checks out a bike (removes it by id) from the bikes list
# Parameters: id (int)
# Returns: nothing

def check_out(id):
	station['bikes'].remove(id)

print('')

print('Question 3 - COMPLETED')
# Create a function 'check_in' that returns a bike (adding it by id) to the bikes list.
# Parameters: id (int)
# Returns: nothing

def check_in(id):
	station['bikes'].append(id)

print('')

print('Question 4 - COMPLETED')
# Congratulations! Your business is expanding. You want to create multiple stations around the city.
# Create a class BikeStation that has the data (name, address, bikes) and all the functions (add, check_out, check_in)
# Parameters to create object: name (string) and address (string)
# Returns: BikeStation Object

class BikeStation():
	"""An object to model a bike rental station"""

	def __init__(self, name, address):
		self.name = name
		self.address = address
		self.bikes = []

	"""Add a bike to the station's inventory"""
	def add_a_bike(self, id):
		self.bikes.append(id)

	"""Simulate checking out a bike"""
	def check_out(self, id):
		self.bikes.remove(id)

	"""Simulate checking out a bike"""
	def check_in(self, id):
		self.bikes.append(id)

print('')

print('Question 5 - COMPLETED')
# You will create station objects using BikeStation class and save them to variables.
# 5.1 - First station, name is Station A. Give it an address of your own choosing. 
# 5.2 - Second station, name is Station B. Give it an address of your own choosing.

station_a = BikeStation('Station A', '8888 Pedal Ln')

station_b = BikeStation('Station B', '9768 Uphill Dr')

print('')

print('Question 6 - COMPLETED')
# 6.1 - Add bikes 1, 2, 3 to Station A. 
# 6.2 - Add bikes 4, 5, 6 to Station B.
# Print the bikes attributes for both Station A and Station B objects.

for i in range(3):
	station_a.add_a_bike(i)
	station_b.add_a_bike(i + 3)

print(f"Station A Bike Inventory ID's Are:  {station_a.bikes}, and Station B Bike Inventory ID's Are: {station_b.bikes}")


print('')

print('Question 7 - COMPLETED')
# 7.1 - Check out bike 3 from Station A
# 7.2 - Check out bike 5 from  Station B
# 7.3 - Check in bike 3 to Station B 
# Print the bikes attributes for both Station A and Station B objects.

station_a.check_out(2)
station_b.check_out(5)
station_b.check_in(2)

print(f"Station A Bike Inventory ID's Are:  {station_a.bikes}, and Station B Bike Inventory ID's Are: {station_b.bikes}")

print()