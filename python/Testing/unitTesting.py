import unittest
"""
Importing unittest, and creating a classes that inherits TestCast from it.
Using various methods from TestCast to test Python internal methods, and custom functions.
Each instance method must contain "test" in name, conventionally, at the beginning.
Each . is a resulting test.
assertEqual takes 2 arguments: the test, and expected result.
The last argument of an assertion is a custom message for when a test fails.
"""

# in practice, these functions should be imported from other module.


def multiply(a, b):
    return a * b


def copy_and_add_element(values, element):
    copy = values[:]
    copy.append(element)
    return copy


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


if __name__ == "__main__":
    unittest.main()
