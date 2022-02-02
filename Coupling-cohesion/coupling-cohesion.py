import string
import random

# Define a Class for all the info about the vehicle
class VehicleInfo:

    # Constructor method for VehicleInfo class with a brand, category and a catalogue_price
    def __init__(self,brand, catalogue_price, category):
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.category = category
    
    # method to compute the tax depending on the category
    def compute_tax(self):
        tax_percentage = float
        if self.category == "car":
            tax_percentage = 0.4
        elif self.category == "motorcycle":
            tax_percentage = 0.2
        elif self.category == 'truck':
            tax_percentage = 1.0
        return tax_percentage * self.catalogue_price
    
    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Tax: {self.compute_tax()}")

# Generate a vehicle object
class Vehicle:
    
    # Constructor method for info about the vehicle
    def __init__(self, license_plate, info, id):
        self.license_plate = license_plate
        self.info = info
        self.id = id
    
    def print(self):
        print(f'Vehicle ID: {self.id}')
        print(f"License plate: {self.license_plate}")
        self.info.print()
    

#Registry of a vehicle
class VehicleRegistry:

    def __init__(self):
        self.vehicle_info = {}
        self.add_vehicle('Ford', 'car', 20000)
        self.add_vehicle('Honda', 'car', 15000)
        self.add_vehicle('Yamaha', 'motorcycle', 5000)
        self.add_vehicle('Suzuki', 'motorcycle', 3000)
        self.add_vehicle('Volvo', 'truck', 50000)
        self.add_vehicle('Mercedes', 'truck', 100000)

    # Add a vehicle to the registry
    def add_vehicle(self, brand, category, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, catalogue_price, category)
        
    # generate the id for the vehicle using random letters
    def generate_vehicle_id(self,length):
        return ''.join(random.choices(string.ascii_uppercase, k = length))
    
    # generate the license plate for the vehicle using random letters and the first 2 letters from the id
    def generate_vehicle_license_plate(self,id):
        return f"{id[:2]}-{''.join(random.choices(string.ascii_uppercase, k=3))}-{''.join(random.choices(string.ascii_uppercase, k=3))}"

    def create_vehicle(self,brand):
        id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license_plate(id)
        return Vehicle(license_plate, self.vehicle_info[brand], id)

class Application:
    
    def register_vehicle(self,  brand: string):
        #create a registry instance
        
        registry = VehicleRegistry()
        vehicle = registry.create_vehicle(brand)

        #show every info about the vehicle
        vehicle.print()

app = Application()
app.register_vehicle('Yamaha')