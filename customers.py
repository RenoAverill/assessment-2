# IMPORTS
import csv
import random

# CREATE A CUSTOMER CLASS
class Customers():
    def __init__(self):
        pass
    

    customer_data = []


# --------------------------------------------
# CREATE A METHOD THAT ALLOWS USER TO INPUT A NEW CUSTOMER

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


# --------------------------------------------
# CREATE A METHOD THAT CHECKS THE COUNT OF MOVIES A CUSTOMER HAS

    def check_customer_vid_count(self, id):
        with open("./data/customers.csv") as csv_file:
            customers = csv.DictReader(csv_file)
            for info in customers:
                if info['id'] == id:
                    movies = info['current_video_rentals']
                    return len(list(movies.split('/')))
                else:
                    return 0

# --------------------------------------------
# CREATE A METHOD THAT RETURNS CURRENT CUSTOMER MOVIES

    def get_customer_vids(self):
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

# --------------------------------------------
# CREATE A METHOD THAT UPDATES CUSTOMER DATA
    def get_customer_data(self):

        with open("./data/customers.csv") as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                customer_obj_data = {}
                customer_obj_data['id'] = line['id']
                customer_obj_data['first_name'] = line['first_name']
                customer_obj_data['last_name'] = line['last_name']
                customer_obj_data['current_video_rentals'] = line['current_video_rentals']
                self.customer_data.append(customer_obj_data)
                

# -------------------------------------------
# SET UPDATED CUSTOMER DATA TO CSV FILE
    def set_customer_data(self, video, id):
        self.get_customer_data()
        header = ['id', 'first_name', 'last_name', 'current_video_rentals']
        for obj in self.customer_data:
            if obj['id'] == id:
                obj['current_video_rentals'] = video
        with open("./data/customers.csv", 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=header)
            writer.writeheader()
            for data in self.customer_data:
                writer.writerow(data)