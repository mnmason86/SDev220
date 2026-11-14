# Mandy Mason | M03_case_study.py

# This program will create a Vehicle super class and an Automobile subclass. The program will accept user input for a car and output the data in an easy-to-read format.

# Variables:
    # vehicle_type: a string that represents the type of vehicle (e.g., car, truck, plane, boat, or broomstick)
    # year: an integer that represents the year of the car
    # make: a string that represents the make of the car
    # model: a string that represents the model of the car
    # doors: an integer that represents the number of doors on the car (2 or 4)
    # roof: a string that represents the type of roof on the car (solid or sun roof)
    
# ------------------

# Write a Python app that has the following classes:
# A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        
# A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
# year
# make
# model
# doors (2 or 4)
# roof (solid or sun roof).

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        

def get_user_input(prompt, valid_options=None):
    while True:
        user_input = input(prompt)
        if prompt == "Enter the year of the car: ":
            try:
                year = int(user_input)
                if 1886 <= year <= 2027:
                    return year
                else:
                    print("Invalid year. Please enter a year between 1886 and 2027.")
            except ValueError:
                print("Invalid input. Please enter a valid year.")
        elif valid_options and user_input not in valid_options:
            print(f"Invalid input. Please choose from {valid_options}.")
        else:
            return user_input

# Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 

def build_car():
    vehicle_type = "car"
    
    # The app will then ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes above.
            
    year = get_user_input("Enter the year of the car: ", "a year between 1886 and 2027")
    make = get_user_input("Enter the make of the car: ")
    model = get_user_input("Enter the model of the car: ")
    doors = int(get_user_input("Enter the number of doors (2 or 4): ", ["2", "4"]))
    roof = get_user_input("Enter the type of roof (solid or sun roof): ", ["solid", "sun roof"])

    car = Automobile(vehicle_type, year, make, model, doors, roof)
    
    # The app will then output the data in an easy-to-read and understandable format, such as this:
    #   Vehicle type: car
    #   Year: 2022
    #   Make: Toyota
    #   Model: Corolla
    #   Number of doors: 4
    #   Type of roof: sun roof

    try:
        print(f"Vehicle type: {car.vehicle_type}")
        print(f"Year: {car.year}")
        print(f"Make: {car.make}")
        print(f"Model: {car.model}")
        print(f"Number of doors: {car.doors}")
        print(f"Type of roof: {car.roof}")
    except ValueError as e:
        print(e)
        
build_car()
        