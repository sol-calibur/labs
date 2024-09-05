class Vehicle:
	def __init__(self, vehicle_type):
		self.vehicle_type = vehicle_type

class Automobile(Vehicle):
	def __init__(self, vehicle_type, year, make, model, doors, roof):
		super().__init__(vehicle_type)
		self.year = year
		self.make = make
		self.model = model
		self.doors = doors
		self.roof = roof

def main():
	vehicle_type = "car"
	year = input("Year of the car: ")
	make = input("Make of the car: ")
	model = input("Model of the car: ")
	doors = input("Number of doors (choose 2 or 4): ")
	roof = input("Enter the type of roof (solid or sun roof): ")

	car = Automobile(vehicle_type, year, make, model, doors, roof)

	print("\nVehicle type:", car.vehicle_type)
	print("Year:", car.year)
	print("Make:", car.make)
	print("Model:", car.model)
	print("Number of doors:", car.doors)
	print("Type of roof:", car.roof)

if __name__ == "__main__":
	main()

