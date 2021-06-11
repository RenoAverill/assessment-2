# import libraries needed
import csv
import random

# Create a Customer class
class Customers():
    def __init__(self, id, first_name, last_name, current_video_rentals):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals

    # Create a method that allows employee to add a new customer
    def set_customer(self):
        # set and get customer data
        self.id = random.randint(10, 999)
        self.first_name = input("\nEnter First Name: ")
        self.last_name = input("\nEnter Last Name: ")
        self.current_video_rentals = 0
        # create a customer data OBJ to append into csv
        customer_data = {'id': self.id, "first_name": self.first_name, "last_name": self.last_name, "current_video_rentals": self.current_video_rentals}
        # access customer csv filer
        with open("./data/customers.csv", 'a') as csv_file:
            header = ['id', 'first_name', 'last_name', 'current_video_rentals']
            customers = csv.DictWriter(csv_file, fieldnames=header)
            # add new customer to csv file
            customers.writerow(customer_data)
            # alert user
            return print("\nNew Customer set!")

    # Create a method that checks how many videos a customer has
    def check_customer_vid_count(self, id):
        # access customer info in csv file
        with open("./data/customers.csv") as csv_file:
            header = ['id', 'first_name', 'last_name', 'current_video_rentals']
            customers = csv.DictReader(csv_file, fieldnames=header)
            # loop through customer info
            for info in csv_file:
                if info[0] == id:
                    print('this works')
                    movies = info['current_video_rentals']
                    return len(list(movies.split('/')))
                else:
                    return 0


    def check_customer_vids(self):
        id = input("\n Enter Customer id: ")
        # access customer info in csv file
        with open("./data/customers.csv") as csv_file:
            header = ['id', 'first_name', 'last_name', 'current_video_rentals']
            customers = csv.DictReader(csv_file, fieldnames=header)
            # loop through customer info
            for info in customers:
                if info["id"] == id:
                    movies = info['current_video_rentals']
                    return print(f"{info['first_name']} has: {movies} currently rented")
                    