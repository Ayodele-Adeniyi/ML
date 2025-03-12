# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 02:00:16 2024

@author: Ayodele Adeniyi
"""

# We Import  the two libraries that will be needed
from datetime import datetime
import re

# This is the list we store our fleet, customers, and shipments.
# These will serve as data storage for the operations and instances
fleet = []
customers = []
shipments = []

# We defined the Vehicle class
class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, vehicle_capacity):
        # Assigning value to the instance of the variable
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.vehicle_capacity = vehicle_capacity
        
# We define the method to update the vehicle information
    def update_vehicle_info(self, vehicle_type, vehicle_capacity):
        # Update the vehicle's type and capacity
        self.vehicle_type = vehicle_type
        self.vehicle_capacity = vehicle_capacity

# We define the Customer class
class Customer:
    def __init__(self, customer_id, name, dob, address, contact_info):
        # Initialize the customer with an ID, name, date of birth, address, and contact information
        self.customer_id = customer_id
        self.name = name
        self.dob = dob
        self.address = address
        self.contact_info = contact_info
        
# The method we use to update the customer information using the attributes, name, address and contact information
    def update_customer_info(self, name, address, contact_info):
        # Update the customer's name, address, and contact information
        self.name = name
        self.address = address
        self.contact_info = contact_info

# We define the Shipment class
class Shipment:
    def __init__(self, shipment_id, origin, destination, weight, vehicle_id, customer_id, status="In transit", delivery_date=None):
        # Initialize the shipment with an ID, origin, destination, weight, vehicle ID, customer ID, status, and delivery date
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.vehicle_id = vehicle_id
        self.customer_id = customer_id
        self.status = status
        self.delivery_date = delivery_date

# The method we use to update the shipment status using the status and delivery date
    def update_shipment_status(self, status, delivery_date):
        # Update the shipment's status and delivery date
        self.status = status
        self.delivery_date = delivery_date

# We create lists to store our fleet, customers, and shipments.
#These are 3 data storage bucket that will be used throughout this project
fleet = []
customers = []
shipments = []

# The following are the functions for Fleet Management
# We use the add_vehicle function to add a new vehicle to the fleet list
def add_vehicle(fleet):
    # Prompt  for vehicle details and add it to the fleet
    while True:
        vehicle_id = input("Enter Vehicle ID (alphanumeric, 4-10 characters): ")
        # Using conditional statement to validate the Vehicle ID with regular expression
        # We use If-statement for conditioning throughout the  assessment
        if re.match("^[a-zA-Z0-9]{4,10}$", vehicle_id):
            break
        else:
            print("Invalid Vehicle ID. It must be alphanumeric and 4-10 characters long.")

    vehicle_type = input("Enter Vehicle Type: ")
    
    while True:
     vehicle_capacity = input("Enter Vehicle Capacity (positive integer): ")
     # To validate that the Vehicle Capacity is a positive integer
     if vehicle_capacity.isdigit() and int(vehicle_capacity) > 0:
         vehicle_capacity = int(vehicle_capacity)
         break
     else:
         print("Invalid input. Please enter a positive integer for Vehicle Capacity.")
 
    new_vehicle = Vehicle(vehicle_id, vehicle_type, vehicle_capacity)
    fleet.append(new_vehicle)
    print(f"Vehicle {vehicle_id} added successfully.")
    
# We use the update_vehicle_info function to update the information of an existing vehicle in the fleet
def update_vehicle_info(fleet):
    # Prompt user for vehicle ID and update its information
    vehicle_id = input("Enter Vehicle ID to update: ")
    for vehicle in fleet:
        if vehicle.vehicle_id == vehicle_id:
            vehicle_type = input("Enter new Vehicle Type: ")
            vehicle_capacity = int(input("Enter new Vehicle Capacity: "))
            vehicle.update_vehicle_info(vehicle_type, vehicle_capacity)
            print("Vehicle updated successfully!")
            return
    print("Vehicle ID not found.")

# We are using the remove_vehicle function is used to remove a vehicle from the fleet
def remove_vehicle(fleet):
    # Prompt user for vehicle ID and remove it from the fleet
    vehicle_id = input("Enter Vehicle ID to remove: ")
    for vehicle in fleet:
        if vehicle.vehicle_id == vehicle_id:
            fleet.remove(vehicle)
            print("Vehicle removed successfully!")
            return
    print("Vehicle ID not found.")

# The view_all_vehicles function is used to display all vehicles in the fleet
def view_all_vehicles(fleet):
    # Display all vehicles in the fleet
    print("Vehicle ID | Vehicle Type | Vehicle Capacity")
    for vehicle in fleet:
        print(f"{vehicle.vehicle_id} | {vehicle.vehicle_type} | {vehicle.vehicle_capacity}")
        
#The Following function are used to handle the functionsoperaetions around  Customer Management
# The add_customer function is used to add a customer to the list of customers
def add_customer(customers):
    # Prompt user for customer details and add it to the list
    while True:
     customer_id = input("Enter Customer ID (alphanumeric, 6-12 characters): ")
     # Validate Customer ID using regular expression
     if re.match("^[a-zA-Z0-9]{4,10}$", customer_id):
         break
     else:
         print("Invalid Customer ID. It must be alphanumeric and 4-10 characters long.")
         
    name = input("Enter Name: ")
    while True:
        dob = input("Enter Date of Birth (DD/MM/YYYY): ")
        # Validate Date format for DOB
        dob_valid = re.match(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$", dob)
        if dob_valid:
            dob_date = datetime.strptime(dob, "%d/%m/%Y")
            # Validate Age is more than or equal to 18 Years
            age = (datetime.now() - dob_date).days // 365
            if age >= 18:
                break
            else:
                print("Age must be 18 years or older.")
        else:
            print("Invalid date format. Please enter DOB in DD/MM/YYYY format.")

    address = input("Enter Address (e.g 1.23 Main St, Sydney): ")
       
    while True:
        phone = input("Enter Your 10 digit Phone (e.g., XXXXXXXX): ")
        # Validate phone number format
        if re.match(r"^[0-9]{10}+$", phone):
            break
        else:
            print("Invalid phone number format. It must be 10 digit.")
    while True:
        email = input("Enter Email (e.g., john@example.com): ")
        # Validate email format
        if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            break
        else:
            print("Invalid email format. Please enter a valid email address.")

    contact_info = f"Phone: {phone}, Email: {email}"
    new_customer = Customer(customer_id, name, dob, address, contact_info)
    customers.append(new_customer)
    print("Customer added successfully!")

# The update_customer_info function is used to update the information of an existing customer.
def update_customer_info(customers):
    # Prompt user for customer ID
    customer_id = input("Enter Customer ID to update: ")

    # Validate the Customer ID to ensure it exists in the list of customers
    customer_to_update = None
    for customer in customers:
        if customer.customer_id == customer_id:
            customer_to_update = customer
            break

    if not customer_to_update:
        print("Customer ID not found.")
        return

    # Prompt the user to enter the new details
    new_name = input("Enter new Name: ")

    while True:
        new_dob = input("Enter Date of Birth (DD/MM/YYYY): ")
        dob_valid = re.match(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$", new_dob)
        if dob_valid:
            dob_date = datetime.strptime(new_dob, "%d/%m/%Y")
            age = (datetime.now() - dob_date).days // 365
            if age >= 18:
                break
            else:
                print("Age must be 18 years or older.")
        else:
            print("Invalid date format. Please enter DOB in DD/MM/YYYY format.")

    
    new_address = input("Enter Address (e.g., 123 Main St, Sydney): ")

    for attempt in range(3):
        new_phone = input("Enter Phone (e.g., XXXXXXXX): ")
        if re.match(r"^[0-9]{10}$", new_phone):
            break
        else:
            print("Invalid phone number format. It must be 10 digits.")
            if attempt == 2:
                print("Maximum attempts reached. Update failed.")
                return

    for attempt in range(3):
        new_email = input("Enter Email (e.g., john@example.com): ")
        if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", new_email):
            break
        else:
            print("Invalid email format. Please enter a valid email address.")
            if attempt == 2:
                print("Maximum attempts reached. Update failed.")
                return

    new_contact_info = f"Phone: {new_phone}, Email: {new_email}"
    # Update the corresponding customer object's information
    customer_to_update.name = new_name
    customer_to_update.dob = new_dob
    customer_to_update.address = new_address
    customer_to_update.contact_info = new_contact_info

    print("Customer information updated successfully!")

# The remove_customer function is used to remove a customer from the list of customers
def remove_customer(customers):
    # Prompt user for customer ID
    customer_id = input("Enter Customer ID to remove: ")

    # Validate the Customer ID to ensure it exists in the list of customers
    for customer in customers:
        if customer.customer_id == customer_id:
            # Ask for confirmation before removing the customer
            confirmation = input(f"Are you sure you want to remove customer {customer_id}? (yes/no): ").strip().lower()
            if confirmation == 'yes':
                customers.remove(customer)
                print("Customer removed successfully!")
                return
            else:
                print("Customer removal canceled.")
                return

    # If invalid Customer ID or not confirmed, display an error message
    print("Customer ID not found.")

# The view_all_customers function is used to display all customers in the list
def view_all_customers(customers):
    # Display all customers
    print(bold_underline_text("Customer ID | Name | Address | Contact Information"))
    for customer in customers:
        print(f"{customer.customer_id} | {customer.name} | {customer.address} | {customer.contact_info}")
        

# The view_customer_shipments function is used to display all shipments for a specific customer
def view_customer_shipments(shipments, customers):
    # Prompt user for customer ID and display their shipments
    customer_id = input("Enter Customer ID to view shipments: ")
    if customer_id in [customer.customer_id for customer in customers]:
        print(bold_underline_text("Shipment ID | Origin | Destination | Weight | Vehicle ID | Status | Delivery Date"))
        for shipment in shipments:
            if shipment.customer_id == customer_id:
                print(f"{shipment.shipment_id} | {shipment.origin} | {shipment.destination} | {shipment.weight} | {shipment.vehicle_id} | {shipment.status} | {shipment.delivery_date}")
    else:
        print("Customer ID not found.")
        
# The following are the functions we use for operations around shipment management.       
# The create_shipment function is used to create a new shipment and validate all inputs
def create_shipment(shipments, fleet, customers):
    while True:
        shipment_id = input("Enter Shipment ID (alphanumeric, 4-8 characters): ")
        # if-statement to validate Shipment ID using regular expression
        if re.match("^[a-zA-Z0-9]{4,8}$", shipment_id):
            break
        else:
            print("Invalid Shipment ID. It must be alphanumeric and 4-8 characters long.")

    origin = input("Enter Origin location (e.g., Sydney, NSW, Australia): ")
    destination = input("Enter Destination location (e.g., Melbourne, VIC, Australia): ")
    
# We use the  While-True function loop to validate input.
    while True:
        weight = input("Enter Weight (positive numeric value, e.g., 500): ")
        # The if-statement validate weight to ensure it is a positive numeric value
        if weight.isdigit() and int(weight) > 0:
            weight = int(weight)
            break
        else:
            print("Invalid Weight. Please enter a positive numeric value.")

    # Displaying a list of available vehicles from the fleet
    print("Available Vehicles:")
    for vehicle in fleet:
        print(f"Vehicle ID: {vehicle.vehicle_id}, Type: {vehicle.vehicle_type}, Capacity: {vehicle.vehicle_capacity} kg")

    while True:
        vehicle_id = input("Select Vehicle ID from the list: ")
        # Validate Vehicle ID to ensure it exists in the available vehicles list.
        if vehicle_id in [vehicle.vehicle_id for vehicle in fleet]:
            break
        else:
            print("Invalid Vehicle ID. Please select a valid Vehicle ID from the list.")

    while True:
        customer_id = input("Enter Customer ID: ")
        # Validate Customer ID to ensure it exists in the list of customers
        if customer_id in [customer.customer_id for customer in customers]:
            break
        else:
            print("Invalid Customer ID. Please enter a valid Customer ID.")

# Create a new Shipment object with the provided details and add it to the list of shipments
    new_shipment = Shipment(shipment_id, origin, destination, weight, vehicle_id, customer_id)
    shipments.append(new_shipment)
    print("Shipment created successfully!")


# We use the track_shipment function to track the status of a shipment
def track_shipment(shipments):
    # Prompt user for shipment ID and display its status
    shipment_id = input("Enter Shipment ID to track: ")
    for shipment in shipments:
        if shipment.shipment_id == shipment_id:
            print(f"Shipment Status: {shipment.status}")
            return
    print("Shipment ID not found.")
    
# The view_all_shipments function is used to display all shipments
def view_all_shipments(shipments):
    # Display all shipments
    print(bold_underline_text("Shipment ID | Origin | Destination | Weight | Vehicle ID | Status | Delivery Date"))
    for shipment in shipments:
        print(f"{shipment.shipment_id} | {shipment.origin} | {shipment.destination} | {shipment.weight} | {shipment.vehicle_id} | {shipment.status} | {shipment.delivery_date}")

# The mark_shipment_delivery function is used to mark a shipment as delivered
def mark_shipment_delivery(shipments):
    # Prompt user for shipment ID and mark it as delivered
    shipment_id = input("Enter Shipment ID to mark delivery: ")
    for shipment in shipments:
        if shipment.shipment_id == shipment_id and shipment.status != "Delivered":
            shipment.update_shipment_status("Delivered", datetime.now().strftime("%d/%m/%Y %H:%M"))
            print("Shipment marked as delivered!")
            return
    print("Invalid Shipment ID or already delivered.")
    
# The view_delivery_status function is used to view the delivery status of a shipment
def view_delivery_status(shipments):
    # Prompt user for shipment ID and display its delivery status
    shipment_id = input("Enter Shipment ID to view delivery status: ")
    for shipment in shipments:
        if shipment.shipment_id == shipment_id:
            if shipment.status == "Delivered":
                print(f"Delivery Date: {shipment.delivery_date}")
            else:
                print("Shipment is not yet delivered.")
            return
    print("Shipment ID not found.")

# We use to the underline and bold test
def bold_underline_text(text):
    return f"\033[1m\033[4m{text}\033[0m"

# The main_menu function is used to navigate between different management functions

def main_menu():
    while True:
        print(bold_underline_text("\n MAIN MENU"))
        print("1. Fleet Management")
        print("2. Customer Management")
        print("3. Shipment Management")
        print("4. Delivery Management")
        print("0. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            fleet_management()
        elif choice == "2":
            customer_management()
        elif choice == "3":
            shipment_management()
        elif choice == "4":
            delivery_management()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

# The fleet_management function is used to manage fleet-related tasks
def fleet_management():
    while True:
        print(bold_underline_text("\n Fleet Management"))
        print("1. Add a Vehicle")
        print("2. Update Vehicle Information")
        print("3. Remove a Vehicle")
        print("4. View All Vehicles")
        print("5. Quit Fleet Management")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_vehicle(fleet)
        elif choice == "2":
            update_vehicle_info(fleet)
        elif choice == "3":
            remove_vehicle(fleet)
        elif choice == "4":
            view_all_vehicles(fleet)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
            
# The customer_management function is used to manage customer-related tasks
def customer_management():
    while True:
        print(bold_underline_text("\n Customer Management"))
        print("1. Add a Customer")
        print("2. Update Customer Information")
        print("3. Remove a Customer")
        print("4. View All Customers")
        print("5. View a Customer’s Shipments")
        print("6. Quit Customer Management")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_customer(customers)
        elif choice == "2":
            update_customer_info(customers)
        elif choice == "3":
            remove_customer(customers)
        elif choice == "4":
            view_all_customers(customers)
        elif choice == "5":
            view_customer_shipments(shipments, customers)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

# The shipment_management function is used to manage shipment-related tasks
def shipment_management():
    while True:
        print(bold_underline_text("\n Shipment Management"))
        print("1. Create a New Shipment")
        print("2. Track a Shipment")
        print("3. View All Shipments")
        print("4. Quit Shipment Management")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_shipment(shipments, fleet, customers)
        elif choice == "2":
            track_shipment(shipments)
        elif choice == "3":
            view_all_shipments(shipments)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# The delivery_management function is used to manage delivery-related tasks
def delivery_management():
    while True:
        print(bold_underline_text("\n Delivery Management"))
        print("1. Mark Shipment Delivery")
        print("2. View Delivery Status for a Shipment")
        print("3. Quit Delivery Management")
        choice = input("Enter your choice: ")

        if choice == "1":
            mark_shipment_delivery(shipments)
        elif choice == "2":
            view_delivery_status(shipments)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

# The main entry point of the assessment program
# Here we call the main menu to start the application 
if __name__ == "__main__":
    main_menu()
