""" The baseclass for all data """


class Data(object):
    """ The most basic form of data """

    def __init__(self, data=None):
        """ Initialise the data """
        self._data = data

    def get_data(self):
        """ Returns the data """
        return self._data

    def set_data(self, new_data=None):
        """ Modifies the data """
        self._data = new_data


class IntegerData(object):
    """ Data that can only be an integer """

    def __init__(self, data=0):
        """ Initialise the data """
        try:
            self._data = int(data)
        except ValueError:
            self._data = 0

    def set_data(self, new_data=0):
        """ Modifies the data """
        try:
            self._data = int(new_data)
        except ValueError:
            pass

    def get_data(self):
        """ Returns the data """
        return self._data


class BooleanData(object):
    """ Data that can only be a boolean """

    def __init__(self, data=False):
        """ Initialise the data """
        if data:
            self._data = True
        else:
            self._data = False

    def set_data(self, new_data=0):
        """ Modifies the data """
        if new_data:
            self._data = True
        else:
            self._data = False

    def get_data(self):
        """ Returns the data """
        return self._data


class FloatData(object):
    """ Data that can only be a float """

    def __init__(self, data=0):
        """ Initialise the data """
        try:
            self._data = float(data)
        except ValueError:
            self._data = 0

    def set_data(self, new_data=0):
        """ Modifies the data """
        try:
            self._data = float(new_data)
        except ValueError:
            pass

    def get_data(self):
        """ Returns the data """
        return self._data


class StringData(object):
    """ Data that can only be a string """

    def __init__(self, data=""):
        """ Initialise the data """
        self._data = str(data)

    def set_data(self, new_data=""):
        """ Modifies the data """
        self._data = str(new_data)

    def get_data(self):
        """ Returns the data """
        return self._data
