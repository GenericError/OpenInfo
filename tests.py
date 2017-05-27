import unittest
import data.basicdata

class TestBaseData(unittest.TestCase):
    """ Testing data.basicdata.Data """

    def test_no_data(self):
        """ Testing None """
        test_data = data.basicdata.Data()
        test_data.get_data()
        test_data.set_data()
        test_data.get_data()

    def test_int_data(self):
        """ Testing integers """
        test_data = data.basicdata.Data(123)
        test_data.get_data()
        test_data.set_data(456)
        test_data.get_data

    def test_float_data(self):
        """ Testing floats """
        test_data = data.basicdata.Data(1.23)
        test_data.get_data()
        test_data.set_data(4.56)
        test_data.get_data

    def test_string_data(self):
        """ Testing strings """
        test_data = data.basicdata.Data("foo")
        test_data.get_data()
        test_data.set_data("bar")
        test_data.get_data()

    def test_list_data(self):
        """ Testing lists """
        test_data = data.basicdata.Data(['foo', '123'])
        test_data.get_data()
        test_data.set_data(['bar', '456'])
        test_data.get_data()

    def test_tuple_data(self):
        """ Testing tuples """
        test_data = data.basicdata.Data(('foo', '123'))
        test_data.get_data()
        test_data.set_data(('bar', '456'))
        test_data.get_data()

    def test_dict_data(self):
        """ Testing dictionary """
        test_data = data.basicdata.Data({'foo': 123})
        test_data.get_data()
        test_data.set_data({'bar': 456})
        test_data.get_data()

    def test_object_data(self):
        """ Testing object """
        more_data = data.basicdata.Data("foobar")
        even_more_data = data.basicdata.Data(['foo', '123'])
        test_data = data.basicdata.Data(more_data)
        test_data.get_data()
        test_data.set_data(even_more_data)
        test_data.get_data()

class TestIntegerData(unittest.TestCase):
    """ Testing data.basicdata.IntegerData """

    def test_no_data(self):
        """ Testing behaviour when no data is given """
        test_data = data.basicdata.IntegerData()
        self.assertEqual(test_data.get_data(), 0)

    def test_integer_data(self):
        """ Testing behaviour when an integer is given """
        test_data = data.basicdata.IntegerData(123)
        self.assertEqual(test_data.get_data(), 123)
        test_data.set_data(456)
        self.assertEqual(test_data.get_data(), 456)

    def test_float_data(self):
        """ Testing behaviour when a float is given """
        test_data = data.basicdata.IntegerData(1.23)
        self.assertEqual(test_data.get_data(), 1)
        test_data.set_data(4.56)
        self.assertEqual(test_data.get_data(), 4)

    def test_non_integer_string_data(self):
        """ Testing beaviour when a string of non-integers is given """
        test_data = data.basicdata.IntegerData("foo")
        self.assertEqual(test_data.get_data(), 0)
        test_data.set_data("bar")
        self.assertEqual(test_data.get_data(), 0)

    def test_integer_string_data(self):
        """ Testing behaviour when a string of integers is given """
        test_data = data.basicdata.IntegerData("123")
        self.assertEqual(test_data.get_data(), 123)
        test_data.set_data("456")
        self.assertEqual(test_data.get_data(), 456)

    def test_no_override(self):
        """ Testing that providing incompatible data
        will not change prexisting data """
        test_data = data.basicdata.IntegerData(123)
        self.assertEqual(test_data.get_data(), 123)
        test_data.set_data("foobar")
        self.assertEqual(test_data.get_data(), 123)


class TestBooleanData(unittest.TestCase):
    """ Testing data.basicdata.BooleanData """

    def test_no_data(self):
        """ Testing behaviour when no data is given """
        test_data = data.basicdata.BooleanData()
        self.assertEqual(test_data.get_data(), False)

    def test_integer_data(self):
        """ Testing behaviour when an integer is given """
        test_data = data.basicdata.BooleanData(1)
        self.assertEqual(test_data.get_data(), True)

    def test_true_data(self):
        """ Testing behaviour when True given """
        test_data = data.basicdata.BooleanData(True)
        self.assertEqual(test_data.get_data(), True)

    def test_set_true_data(self):
        """ Testing behaviour when the data is changed to True """
        test_data = data.basicdata.BooleanData(False)
        test_data.set_data(True)
        self.assertEqual(test_data.get_data(), True)

    def test_set_false_data(self):
        """ Testing behaviour when the data is changed to False """
        test_data = data.basicdata.BooleanData(True)
        test_data.set_data(False)
        self.assertEqual(test_data.get_data(), False)


class TestFloatData(unittest.TestCase):
    """ Testing data.basicdata.FloatData """

    def test_no_data(self):
        """ Testing behaviour when no data is given """
        test_data = data.basicdata.FloatData()
        self.assertEqual(test_data.get_data(), 0)

    def test_integer_data(self):
        """ Testing behaviour when an integer is given """
        test_data = data.basicdata.FloatData(123)
        self.assertEqual(test_data.get_data(), 123.0)
        test_data.set_data(456)
        self.assertEqual(test_data.get_data(), 456.0)

    def test_float_data(self):
        """ Testing behaviour when a float is given """
        test_data = data.basicdata.FloatData(1.23)
        self.assertEqual(test_data.get_data(), 1.23)
        test_data.set_data(4.56)
        self.assertEqual(test_data.get_data(), 4.56)

    def test_non_integer_string_data(self):
        """ Testing beaviour when a string of non-integers is given """
        test_data = data.basicdata.FloatData("foo")
        self.assertEqual(test_data.get_data(), 0)
        test_data.set_data("bar")
        self.assertEqual(test_data.get_data(), 0)

    def test_integer_string_data(self):
        """ Testing behaviour when a string of integers is given """
        test_data = data.basicdata.FloatData("1.23")
        self.assertEqual(test_data.get_data(), 1.23)
        test_data.set_data("4.56")
        self.assertEqual(test_data.get_data(), 4.56)

    def test_no_override(self):
        """ Testing that providing incompatible data
        will not change prexisting data """
        test_data = data.basicdata.FloatData(1.23)
        self.assertEqual(test_data.get_data(), 1.23)
        test_data.set_data("foobar")
        self.assertEqual(test_data.get_data(), 1.23)


class TestStringData(unittest.TestCase):
    """ Testing data.basicdata.StringData """

    def test_no_data(self):
        """ Testing behaviour when no data is given """
        test_data = data.basicdata.StringData()
        self.assertEqual(test_data.get_data(), "")

    def test_integer_data(self):
        """ Testing behaviour when an string is given """
        test_data = data.basicdata.StringData("foo")
        self.assertEqual(test_data.get_data(), "foo")
        test_data.set_data("bar")
        self.assertEqual(test_data.get_data(), "bar")

    def test_float_data(self):
        """ Testing behaviour when a integer is given """
        test_data = data.basicdata.StringData(123)
        self.assertEqual(test_data.get_data(), "123")
        test_data.set_data(456)
        self.assertEqual(test_data.get_data(), "456")

if __name__ == '__main__':
    unittest.main()
