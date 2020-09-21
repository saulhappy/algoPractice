import unittest
"""
Importing unittest, and creating a classes that inherits TestCast from it.
Using various methods from TestCast to test Python internal methods, and custom functions.
Each instance method must contain "test" in name, conventionally, at the beginning.
Each . is a resulting test.
assertEqual takes 2 arguments: the test, and expected result.
The last argument of an assertion is a custom message for when a test fails.

Other assertions not included:
- Equality vs Identify: assertEqual() vs assertIs()/assertIsNot()
- Truthiness vs Falsiness: assertTrue/assertFalse
- Nullness: assertIsNone/assertisNotNone
- Inclusiveness: assertIn/assertNotIn
"""

# in practice, these functions should be imported from other module.


def multiply(a, b):
    return a * b


def copy_and_add_element(values, element):
    copy = values[:]
    copy.append(element)
    return copy


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y


class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        self.assertEqual("d+e+f".split("+"), ["d", "e", "f"])

    def test_count(self):
        self.assertEqual("beautiful".count("u"), 2)


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)

# Testing Skip


class TestSwapCase(unittest.TestCase):
    @unittest.skip("Testing skip method")
    def test_swap_case(self):
        pass

# Testing Equality


class TestInequality(unittest.TestCase):
    def test_inequality(self):
        self.assertNotEqual(1, 2)
        self.assertNotEqual([1, 2], [2, 1])

    def test_copy_and_add_element(self):
        values = [1, 2, 3]
        result = copy_and_add_element(values, 4)

        self.assertEqual(result, [1, 2, 3, 4])

        self.assertNotEqual(
            values,
            [1, 2, 3, 4],
            "The copy_and_add_element function is mutating the input. Make sure you're creating a copy."
        )

# Testing Object Type class


class ObjectTypeTests(unittest.TestCase):
    def test_is_instance(self):
        self.assertIsInstance(1, int)
        self.assertIsInstance(8.765, float)
        self.assertIsInstance([], list)
        self.assertIsInstance({"a": 1}, dict)

        # self.assertIsInstance({ "a": 1 }, list)

    def test_not_is_instance(self):
        self.assertNotIsInstance(5, list)
        self.assertNotIsInstance(5, float)
        self.assertNotIsInstance(5, set)
        self.assertNotIsInstance(5, dict)

        # self.assertNotIsInstance(5, int)

# Testing Errors


class DivideTestCase(unittest.TestCase):

    # one method
    def test_divide(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)

    # alternative method
    def test_divide_another_way(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

# Set up tear downs for testing.


class TestOperations(unittest.TestCase):
    # setupClass runs once. Designed for more "expensive" operations, such as connecting to a databases
    @classmethod
    def setUpClass(cls):
        print("This will run ONCE before the test suite starts")
    # setUp and TearDown will run before/after each test. Designed to do smaller things (like create instance classes with attributes) a test might need.

    def setUp(self):
        print("This will run before EACH test")

    def tearDown(self):
        print("This will run after EACH test")

    # tearDownClass runs once at the end, to do something like close a file, or database connection.
    @classmethod
    def tearDownClass(cls):
        print("This will run ONCE after the test suite finishes")

    def test_stuff(self):
        self.assertEqual(1, 1)

    def test_more_stuff(self):
        self.assertEqual([], [])


if __name__ == "__main__":
    unittest.main()
