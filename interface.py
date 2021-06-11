# import items needed
from os import name
from video import Video
from customers import Customers

class Interface():
    def __init__(self):
        pass
        #Create a running interface function 
    def run(self):

        input = self.main_menu()
        
        # Create a reactive interace
        while True:
            if input == '1':
                return Video.get_video_inventory(self)
            elif input == '2':
                return Customers.check_customer_vids(self)
            elif input == '3':
                return Video.rent_video(self)
            elif input == '4':
                return Video.return_video(self)
            elif input == '5':
                return Customers.set_customer(self)
            elif input == '6':
                print("\n\nHave a great day!")
                break

# Create an interface menu with various options
    def main_menu(self):

        mode = input("\nWelcome to Code Platoon Video!\n1. View video inventory\n2. View customer's rented videos\n3. Rent video\n4. Return video\n5. Add new customer\n6. Exit\n\n")
        return mode