""" Basic data types """


class Data(object):
    """ The most basic form of data """

    def __init__(self, data=None):
        """ Initialise the data """
        self._data = self.set_data(data)

    def get_data(self):
        """ Returns the data """
        return self._data

    def set_data(self, new_data=None):
        """ Modifies the data """
        self._data = new_data


class IntegerData(Data):
    """ Data that can only be an integer """

    def __init__(self, data=0):
        """ Initialise the data """
        Data.__init__(self)
        self._data = self.set_data(data)

    def set_data(self, new_data=0):
        """ Modifies the data """
        try:
            self._data = int(new_data)
        except ValueError:
            pass


class BooleanData(Data):
    """ Data that can only be a boolean """

    def __init__(self, data=False):
        """ Initialise the data """
        Data.__init__(self)
        self._data = self.set_data(data)

    def set_data(self, new_data=False):
        """ Modifies the data """
        self._data = bool(new_data)


class FloatData(Data):
    """ Data that can only be a float """

    def __init__(self, data=0):
        """ Initialise the data """
        Data.__init__(self)
        self._data = self.set_data(data)

    def set_data(self, new_data=0):
        """ Modifies the data """
        try:
            self._data = float(new_data)
        except ValueError:
            pass


class StringData(Data):
    """ Data that can only be a string """

    def __init__(self, data=""):
        """ Initialise the data """
        Data.__init__(self)
        self._data = self.set_data(data)

    def set_data(self, new_data=""):
        """ Modifies the data """
        self._data = str(new_data)
