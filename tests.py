import unittest
import data

class TestBaseData(unittest.TestCase):
    """ Testing data.Data """

    def test_no_data(self):
        """ Testing None """
        test_data = data.Data()
        test_data.get_data()
        test_data.set_data()
        test_data.get_data()

    def test_int_data(self):
        """ Testing integers """
        test_data = data.Data(123)
        test_data.get_data()
        test_data.set_data(456)
        test_data.get_data

    def test_float_data(self):
        """ Testing floats """
        test_data = data.Data(1.23)
        test_data.get_data()
        test_data.set_data(4.56)
        test_data.get_data

    def test_string_data(self):
        """ Testing strings """
        test_data = data.Data("foo")
        test_data.get_data()
        test_data.set_data("bar")
        test_data.get_data()

    def test_list_data(self):
        """ Testing lists """
        test_data = data.Data(['foo', '123'])
        test_data.get_data()
        test_data.set_data(['bar', '456'])
        test_data.get_data()

    def test_tuple_data(self):
        """ Testing tuples """
        test_data = data.Data(('foo', '123'))
        test_data.get_data()
        test_data.set_data(('bar', '456'))
        test_data.get_data()

    def test_dict_data(self):
        """ Testing dictionary """
        test_data = data.Data({'foo': 123})
        test_data.get_data()
        test_data.set_data({'bar': 456})
        test_data.get_data()

    def test_object_data(self):
        """ Testing object """
        more_data = data.Data("foobar")
        even_more_data = data.Data(['foo', '123'])
        test_data = data.Data(more_data)
        test_data.get_data()
        test_data.set_data(even_more_data)
        test_data.get_data()

class TestIntegerData(unittest.TestCase):
    """ Testing data.IntegerData """

    def test_no_data(self):
        """ Testing behaviour when no data is given """
        test_data = data.IntegerData()
        self.assertEqual(test_data.get_data(), 0)

    def test_integer_data(self):
        """ Testing behaviour when an integer is given """
        test_data = data.IntegerData(123)
        self.assertEqual(test_data.get_data(), 123)
        test_data.set_data(456)
        self.assertEqual(test_data.get_data(), 456)

    def test_float_data(self):
        """ Testing behaviour when a float is given """
        test_data = data.IntegerData(1.23)
        self.assertEqual(test_data.get_data(), 1)
        test_data.set_data(4.56)
        self.assertEqual(test_data.get_data(), 4)

    def test_non_integer_string_data(self):
        """ Testing beaviour when a string of non-integers is given """
        test_data = data.IntegerData("foo")
        self.assertEqual(test_data.get_data(), 0)
        test_data.set_data("bar")
        self.assertEqual(test_data.get_data(), 0)

    def test_integer_string_data(self):
        """ Testing behaviour when a string of integers is given """
        test_data = data.IntegerData("123")
        self.assertEqual(test_data.get_data(), 123)
        test_data.set_data("456")
        self.assertEqual(test_data.get_data(), 456)

    def test_no_override(self):
        """ Testing that providing incompatible data
        will not change prexisting data """
        test_data = data.IntegerData(123)
        self.assertEqual(test_data.get_data(), 123)
        test_data.set_data("foobar")
        self.assertEqual(test_data.get_data(), 123)


class TestBooleanData(unittest.TestCase):
    """ Testing data.BooleanData """

    def test_no_data(self):
        """ Testing behaviour when no data is given """
        test_data = data.BooleanData()
        self.assertEqual(test_data.get_data(), False)

    def test_integer_data(self):
        """ Testing behaviour when an integer is given """
        test_data = data.BooleanData(1)
        self.assertEqual(test_data.get_data(), True)

    def test_true_data(self):
        """ Testing behaviour when True given """
        test_data = data.BooleanData(True)
        self.assertEqual(test_data.get_data(), True)

    def test_set_true_data(self):
        """ Testing behaviour when the data is changed to True """
        test_data = data.BooleanData(False)
        test_data.set_data(True)
        self.assertEqual(test_data.get_data(), True)

    def test_set_false_data(self):
        """ Testing behaviour when the data is changed to False """
        test_data = data.BooleanData(True)
        test_data.set_data(False)
        self.assertEqual(test_data.get_data(), False)


class TestFloatData(unittest.TestCase):
    """ Testing data.floatData """

    def test_no_data(self):
        """ Testing behaviour when no data is given """
        test_data = data.FloatData()
        self.assertEqual(test_data.get_data(), 0)

    def test_integer_data(self):
        """ Testing behaviour when an integer is given """
        test_data = data.FloatData(123)
        self.assertEqual(test_data.get_data(), 123.0)
        test_data.set_data(456)
        self.assertEqual(test_data.get_data(), 456.0)

    def test_float_data(self):
        """ Testing behaviour when a float is given """
        test_data = data.FloatData(1.23)
        self.assertEqual(test_data.get_data(), 1.23)
        test_data.set_data(4.56)
        self.assertEqual(test_data.get_data(), 4.56)

    def test_non_integer_string_data(self):
        """ Testing beaviour when a string of non-integers is given """
        test_data = data.FloatData("foo")
        self.assertEqual(test_data.get_data(), 0)
        test_data.set_data("bar")
        self.assertEqual(test_data.get_data(), 0)

    def test_integer_string_data(self):
        """ Testing behaviour when a string of integers is given """
        test_data = data.FloatData("1.23")
        self.assertEqual(test_data.get_data(), 1.23)
        test_data.set_data("4.56")
        self.assertEqual(test_data.get_data(), 4.56)

    def test_no_override(self):
        """ Testing that providing incompatible data
        will not change prexisting data """
        test_data = data.FloatData(1.23)
        self.assertEqual(test_data.get_data(), 1.23)
        test_data.set_data("foobar")
        self.assertEqual(test_data.get_data(), 1.23)

if __name__ == '__main__':
    unittest.main()
