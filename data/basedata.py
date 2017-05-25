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
