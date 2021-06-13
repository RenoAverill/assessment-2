# import items needed

from video import *
from customers import *

class Interface(Video, Customers):
    def __init__(self):
        pass
        #Create a running interface function 
    def run(self):
        # Create a reactive interace
        while True:
            input = self.main_menu()
            if input == '1':
                Video.get_total_inventory(self)
            elif input == '2':
                Customers.get_customer_vids(self)
            elif input == '3':
                Video.rent_video(self)
            elif input == '4':
                Video.return_video(self)
            elif input == '5':
                Customers.set_customer(self)
            elif input == '6':
                print("\n\nHave a great day!")
                break
            
# Create an interface menu with various options
    def main_menu(self):

        mode = input("\nWelcome to Code Platoon Video!\n1. View video inventory\n2. View customer's rented videos\n3. Rent video\n4. Return video\n5. Add new customer\n6. Exit\n\n")
        return mode