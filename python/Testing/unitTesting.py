import unittest
"""
Importing unittest, and creating a class that inherits TestCast from it. 
Using assertEqual to test Python's split and count functions.
Each instance method must contain "test" in name, conventionally, at the beginning. 
Each . is a resulting test. 
assertEqual takes 2 arguments: the test, and expected result. 
"""


class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        self.assertEqual("d+e+f".split("+"), ["d", "e", "f"])

    def test_count(self):
        self.assertEqual("beautiful".count("u"), 2)


if __name__ == "__main__":
    unittest.main()
