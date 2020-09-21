import unittest
"""
Importing unittest, and creating a class that inherits TestCast from it.
Using assertEqual to test Python's split and count functions.
Each instance method must contain "test" in name, conventionally, at the beginning.
Each . is a resulting test.
assertEqual takes 2 arguments: the test, and expected result.
"""


def multiply(a, b):
    return a * b


class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        self.assertEqual("d+e+f".split("+"), ["d", "e", "f"])

    def test_count(self):
        self.assertEqual("beautiful".count("u"), 2)


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)


class TestSwapCase(unittest.TestCase):
    @unittest.skip("Testing skip method")
    def test_swap_case(self):
        pass


if __name__ == "__main__":
    unittest.main()
