"""Import Unittest and mymodule.py and test the functions square and double in mymodule.py."""
import unittest

from mymodule import square, double, add


class TestSquare(unittest.TestCase):
    """This is a class called TestSquare to test the function square in mymodule.py."""

    def test1(self):
        """The following tests the function square in mymodule.py."""
        self.assertEqual(
            square(2), 4)  # test when 2 is given as input the output is 4.
        # test when 3.0 is given as input the output is 9.0.
        self.assertEqual(square(3.0), 9.0)
        # test when -3 is given as input the output is not -9.
        self.assertNotEqual(square(-3), -9)


class TestDouble(unittest.TestCase):
    """This is a class called TestDouble to test the function double in mymodule.py."""
    def test1(self):
        """This is a function called test1 to test the function double in mymodule.py."""
        # test when 2 is given as input the output is 4.
        self.assertEqual(double(2), 4)
        # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(double(-3.1), -6.2)
        # test when 0 is given as input the output is 0.
        self.assertEqual(double(0), 0)


class TestAdd(unittest.TestCase):
    """This is a class called TestAdd to test the function add in mymodule.py."""
    def test1(self):
        """This is a function called test1 to test the function add in mymodule.py."""
        self.assertEqual(add(2, 4), 6)  # test when 2 and 3 are given as input the output is 5.
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(2.3, 3.6), 5.9)
        self.assertEqual(add('hello', 'world'), 'helloworld')
        self.assertEqual(add(2.3000, 4.3000), 6.6)
        self.assertNotEqual(add(-2, -2), 0)


unittest.main()
