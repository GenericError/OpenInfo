import unittest
import data.basedata

class BaseData(unittest.TestCase):
    """ Testing data.basedata.BaseData """

    def test_no_data(self):
        """ Testing None """
        test_data = data.basedata.BaseData()
        test_data.get_data()
        test_data.set_data()
        test_data.get_data()

    def test_int_data(self):
        """ Testing integers """
        test_data = data.basedata.BaseData(123)
        test_data.get_data()
        test_data.set_data(456)
        test_data.get_data

    def test_float_data(self):
        """ Testing floats """
        test_data = data.basedata.BaseData(1.23)
        test_data.get_data()
        test_data.set_data(4.56)
        test_data.get_data

    def test_string_data(self):
        """ Testing strings """
        test_data = data.basedata.BaseData("foo")
        test_data.get_data()
        test_data.set_data("bar")
        test_data.get_data()

    def test_list_data(self):
        """ Testing lists """
        test_data = data.basedata.BaseData(['foo', '123'])
        test_data.get_data()
        test_data.set_data(['bar', '456'])
        test_data.get_data()

    def test_tuple_data(self):
        """ Testing tuples """
        test_data = data.basedata.BaseData(('foo', '123'))
        test_data.get_data()
        test_data.set_data(('bar', '456'))
        test_data.get_data()

    def test_dict_data(self):
        """ Testing dictionary """
        test_data = data.basedata.BaseData({'foo': 123})
        test_data.get_data()
        test_data.set_data({'bar': 456})
        test_data.get_data()

    def test_object_data(self):
        """ Testing object """
        more_data = data.basedata.BaseData("foobar")
        even_more_data = data.basedata.BaseData(['foo', '123'])
        test_data = data.basedata.BaseData(more_data)
        test_data.get_data()
        test_data.set_data(even_more_data)
        test_data.get_data()

if __name__ == '__main__':
    unittest.main()
