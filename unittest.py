from video import Video
from customers import Customers
import unittest

class TestStringMethods(unittest.TestCase):
    # create a test to see if the method check customer vid count is an int
    def test_int(self):
        video = Customers.check_customer_vid_count(self)
        self.assertEqual(type(video), int)
    # create a test to see if a video is still in stock
    def test_availability(self):
        count = Video.check_availibility(self)
        self.assertEqual(type(count), int)
    # create a test that checks customers video inventory
    def test_inventory(self):
        inventory = Customers.check_customer_vids(self)
        self.assertTrue(inventory)
    # create a test that checks renting
    def test_int(self):
        rent = Video.rent_video(self)
        self.assertTrue(rent)

if __name__ == '__main__':
    unittest.main()
