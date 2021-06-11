# import csv and other info needed
import csv
from customers import Customers

# Create a Video class with various methods
class Video():
    def __init__(self) -> None:
        pass
    #Create a methods that returns a list of all active inventory 
    def get_video_inventory(self):
        # accessing into the csv file
        with open("./data/inventory.csv") as csv_file:
            inventory = csv.reader(csv_file)
            # looping through inventory
            for item in inventory:
                print(item)

    # Create a method that allowing rentals to occur
    def rent_video(self):
        # geting video and customer info
        video = input("\nEnter movie to be rented: ")
        id = input("\nEnter Customer id: ")
        # check to see if the customer is uneder max check out value
        # check inventory to see if movie is availible
        if Customers.check_customer_vid_count(self, id) <= 2:
             
            if Video.check_availibility(self, video) > 0:
                count = -1
                Video.update_rentals(self, video, count, id)
                return print(f"Thanks! Hope your enjoy {video}!")
            else:
                return print("Sorry this movie is unavailable right now.")
        else:
            return print("You have too many videos checked out!")
    
    
    # create method that updates inventory csv file for a new rental
    def update_rentals(self, video, count, id):
        with open("./data/inventory.csv", 'a') as csv_file:
            header = ['id', 'title', 'rating', 'copies_available']
            inventory = csv.DictReader(csv_file, fieldnames= header)
            for item in inventory:
                if item['title'] == video:
                    item['copies_available'] += str(count)
    
    
    # Create method that checks movie availibility
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

    
    # create method that allow customer to return video
    def return_video(self):
        # get info from customer
        video = input("\nEnter movie to be returned: ")
        id = input("\nEnter Customer ID: ")
        # increment count
        count = 1
        Video.update_rentals(self, video, count, id)
        # thank the customer!
        return print(f"Thank you for returning {video}!")

    