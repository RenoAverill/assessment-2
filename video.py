# IMPORTS
import csv
from customers import Customers

# CREATE A VIDEO CLASS
class Video():
    def __init__(self):
        pass
    
    inventory_data = []

# --------------------------------------------
# CREATE A METHOD TAHT RETURNS ALL CURRENT INVENTORY

    def get_total_inventory(self):
        with open("./data/inventory.csv") as csv_file:
            reader = csv.DictReader(csv_file)
            for movie in reader:
                print(movie['title'])


    
# --------------------------------------------    
# CREATE A METHOD THAT GETS INTO FROM INVENTORY CSV FILE

    def get_inventory_data(self):

        with open("./data/inventory.csv") as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                inventory_obj_data = {}
                inventory_obj_data['id'] = line['id']
                inventory_obj_data['title'] = line['title']
                inventory_obj_data['rating'] = line['rating']
                inventory_obj_data['copies_available'] = line['copies_available']
                self.inventory_data.append(inventory_obj_data)
                

# --------------------------------------------
# CREATE A METHOD THAT LETS A CUSTOMER RENT A MOVIE

    def rent_video(self):
        maximum_vids = 3
        video = input("\nEnter movie to be rented: ")
        id = input("\nEnter Customer id: ")
        if Customers.check_customer_vid_count(self, id) < maximum_vids:  
            if self.check_availibility(video) > 0:
                count = -1
                Video.set_inventory_data(self, video, count)
                Customers.set_customer_data(self, video, id)
                return print(f"Thanks! Hope your enjoy {video}!")
            else:
                return print("Sorry this movie is unavailable right now.")
        else:
            return print("You have too many videos checked out!")



# --------------------------------------------          
# CREATE A METHOD THAT UPDATES INVENTORY CSV FILE

    def set_inventory_data(self, video, count):
        self.get_inventory_data()
        header = ['id', 'title', 'rating', 'copies_available']
        for obj in self.inventory_data:
            if obj['title'] == video:
                obj['copies_available'] = int(obj['copies_available']) + count
        with open("./data/inventory.csv", 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=header)
            writer.writeheader()
            for data in self.inventory_data:
                writer.writerow(data)
    

# --------------------------------------------    
# CREATE A METHOD THAT CHECKS MOVIE AVILIBILITY

    def check_availibility(self, video):
        # accessing csv file
        with open("./data/inventory.csv") as csv_file:
            header = ['id', 'title', 'rating', 'copies_available']
            inventory = csv.DictReader(csv_file, fieldnames= header)
            # loop through current inventory
            for item in inventory:
                if item['title'] == video:
                    if int(item['copies_available']) > 0:
                        return int(item['copies_available'])
            else:
                return 0

# --------------------------------------------   
# CREATE A METHOD THAT ALLOWS USER TO RETURN A CUSTOMERS MOVIE
# UPDATES CSV FILES

    def return_video(self):
        # get info from customer
        video = input("\nEnter movie to be returned: ")
        id = input("\nEnter Customer ID: ")
        # increment count
        count = 1
        # set new data
        Video.set_inventory_data(video, count)
        Customers.set_customer_data(video, id)
        # thank the customer!
        return print(f"Thank you for returning {video}!")

    