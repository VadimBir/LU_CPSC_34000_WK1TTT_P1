# Have a unit test that would pass if "hello_world.py" executes correctly and fails if it does not.
# The test should also fail if the "hello_world.py" file is missing.
#
import os
import unittest
from hello_world import print_hi

class TestClass(unittest.TestCase):
    def test_file_exits(self):
        print("checking if file exists")
        res = os.path.exists("hello_world.py")
        print("\t\t", res)
        assert res
    def test_output_hello_world(self):
        print("checking if hello world is printed")
        res = print_hi() == "Hello World!"
        print("\t\t", res)
        assert res



if __name__ == '__main__':
    unittest.main()