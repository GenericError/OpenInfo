""" Sets of basic data types """
import basicdata


class Array(basicdata.Data):
    """ Multiple basic data types """
    def __init__(self, list_of_data=None):
        """ Initalise the array """
        basicdata.Data.__init__(self)
        self._data = self.set_data(list_of_data)

    def add_data(self, data_to_add):
        """ Appends data to the array """
        if data_to_add:
            for data in data_to_add:
                if issubclass(basicdata.Data, data_to_add):
                    self._data.append(data)

    def remove_data(self, data_to_remove):
        """ Removes data from the array """
        if data_to_remove:
            for data in data_to_remove:
                self._data.remove(data)

    def set_data(self, list_of_data=None):
        """ Replaces all data in the array with the new data given """
        if list_of_data:
            self.remove_data(self._data)
            self.add_data(list_of_data)


class Dictionary(basicdata.Data):
    """ Multiple named basic data """
    def __init__(self, list_of_data=None):
        """ Initalise the dictionary """
        basicdata.Data.__init__(self)
        self._data = self.set_data(list_of_data)

    def add_data(self, data_to_add):
        """ Appends data to the dictionary """
        if data_to_add:
            for data in data_to_add:
                if issubclass(basicdata.Data, data[1]):
                    self._data[data[0]] = data[1]

    def remove_data(self, data_to_remove):
        """ Removes data from the dictionary """
        if data_to_remove:
            for data in data_to_remove:
                self._data[data[0]] = None

    def set_data(self, list_of_data=None):
        """ Replaces all data in the dictionary with the new data given """
        if list_of_data:
            self.remove_data(self._data)
            self.add_data(list_of_data)
