class DataNode:
    """
    A class representing a node in the Data structure.
    Each node contains data and allows attribute access to nested data using dot notation.
    """

    def __init__(self, data=None):
        """
        Initialize a DataNode with optional data.

        Args:
            data (dict, optional): A dictionary representing the data of the node.
        """
        self._data = data if data is not None else {}

    def __getattr__(self, item):
        """
        Handle attribute access for the DataNode.

        If the attribute is present in the data, it is returned as-is.
        If the attribute is a nested dictionary, a new DataNode is created for it.

        Args:
            item (str): The attribute being accessed.

        Returns:
            Any: The value of the attribute, or a new DataNode for nested dictionaries.

        Note:
            If the attribute is not found in the data, None is returned.
        """
        if item in self._data:
            value = self._data[item]
            if isinstance(value, dict):
                return DataNode(value)
            return value
        return None

    def __setattr__(self, key, value):
        """
        Handle attribute assignment for the DataNode.

        Args:
            key (str): The attribute being assigned.
            value (Any): The value to be assigned to the attribute.

        Note:
            This implementation allows only setting attributes for the data dictionary.
            All other attributes are treated as regular class attributes.
        """
        if key != "_data":
            self._data[key] = value
        else:
            self.__dict__[key] = value

    def __delattr__(self, item):
        """
        Handle attribute deletion for the DataNode.

        Args:
            item (str): The attribute to be deleted from the data.
        """
        if item in self._data:
            del self._data[item]

    def __getitem__(self, item):
        """
        Handle item access for the DataNode.

        If the item is present in the data, it is returned as-is.
        If the item is a nested dictionary, a new DataNode is created for it.

        Args:
            item (str): The item being accessed.

        Returns:
            Any: The value of the item, or a new DataNode for nested dictionaries.

        Raises:
            KeyError: If the item is not present in the data.
        """
        if item in self._data:
            value = self._data[item]
            if isinstance(value, dict):
                return DataNode(value)
            return value
        raise KeyError(f"'{item}' not found in DataNode object.")

    def __setitem__(self, key, value):
        """
        Handle item assignment for the DataNode.

        Args:
            key (str): The item being assigned.
            value (Any): The value to be assigned to the item.
        """
        self._data[key] = value

    def __delitem__(self, item):
        """
        Handle item deletion for the DataNode.

        Args:
            item (str): The item to be deleted from the data.
        """
        if item in self._data:
            del self._data[item]

    def to_dict(self):
        """
        Convert the DataNode to a dictionary.

        Returns:
            dict: A dictionary representation of the DataNode.
        """
        return self._data


class Data:
    """
    A class representing a dynamic data structure.
    The Data class allows creating nested data structures and defining default values for attributes.
    """

    def __init__(self, **kwargs):
        """
        Initialize a Data object with optional data and default_values.

        Args:
            **kwargs: Keyword arguments for initializing the Data object.

        Keyword Args:
            data (dict, optional): A dictionary representing the data of the object.
            default_values (dict, optional): A dictionary containing default values for attributes.
        """
        self._data = kwargs.get("data", {})
        self._default_values = kwargs.get("default_values", {})

    @classmethod
    def from_dict(cls, data):
        """
        Create a Data object from a dictionary.

        Args:
            data (dict): A dictionary representing the data to be loaded.

        Returns:
            Data: A Data object with data loaded from the input dictionary.
        """
        return cls(data=data)

    def __getattr__(self, item):
        """
        Handle attribute access for the Data object.

        If the attribute is present in the data, it is returned as-is.
        If the attribute is a nested dictionary, a new DataNode is created for it.
        If the attribute is a default value, it is set and returned.

        Args:
            item (str): The attribute being accessed.

        Returns:
            Any: The value of the attribute, a new DataNode for nested dictionaries, or a default value.

        Raises:
            AttributeError: If the attribute is not present in the data or default_values.
        """
        if item in self._data:
            value = self._data[item]
            if isinstance(value, dict):
                return DataNode(value)
            return value
        elif item in self._default_values:
            default_value = self._default_values[item]
            self._data[item] = default_value
            return DataNode(default_value)
        else:
            raise AttributeError(f"'Data' object has no attribute '{item}'")

    def __setattr__(self, key, value):
        """
        Handle attribute assignment for the Data object.

        Args:
            key (str): The attribute being assigned.
            value (Any): The value to be assigned to the attribute.

        Note:
            This implementation allows setting attributes for the data dictionary or default_values.
            All other attributes are treated as regular class attributes.
        """
        if key in ["_data", "_default_values"]:
            self.__dict__[key] = value
        else:
            self._data[key] = value

    def __delattr__(self, item):
        """
        Handle attribute deletion for the Data object.

        Args:
            item (str): The attribute to be deleted from the data.

        Raises:
            AttributeError: If the attribute is not present in the data.
        """
        if item in self._data:
            del self._data[item]
        else:
            raise AttributeError(f"'Data' object has no attribute '{item}'")

    def __getitem__(self, item):
        """
        Handle item access for the Data object.

        If the item is present in the data, it is returned as-is.
        If the item is a nested dictionary, a new DataNode is created for it.
        If the item is a default value, it is set and returned.

        Args:
            item (str): The item being accessed.

        Returns:
            Any: The value of the item, a new DataNode for nested dictionaries, or a default value.

        Raises:
            KeyError: If the item is not present in the data or default_values.
        """
        if item in self._data:
            value = self._data[item]
            if isinstance(value, dict):
                return DataNode(value)
            return value
        elif item in self._default_values:
            default_value = self._default_values[item]
            self._data[item] = default_value
            return DataNode(default_value)
        else:
            raise KeyError(f"'{item}' not found in Data object.")

    def __setitem__(self, key, value):
        """
        Handle item assignment for the Data object.

        Args:
            key (str): The item being assigned.
            value (Any): The value to be assigned to the item.
        """
        self._data[key] = value

    def __delitem__(self, item):
        """
        Handle item deletion for the Data object.

        Args:
            item (str): The item to be deleted from the data.

        Raises:
            KeyError: If the item is not present in the data.
        """
        if item in self._data:
            del self._data[item]
        else:
            raise KeyError(f"'{item}' not found in Data object.")

    def to_dict(self):
        """
        Convert the Data object to a dictionary.

        Returns:
            dict: A dictionary representation of the Data object.
        """
        return self._data


data = {
    "id": "1",
    "name": "first",
    "metadata": {
        "system": {
            "size": 10.7
        },
        "user": {
            "batch": 10
        }
    }
}

# load from dict
my_inst_1 = Data.from_dict(data)

# load from inputs
my_inst_2 = Data(name="my")

# reflect inner value
print(my_inst_1.metadata.system.size)  # Output: 10.7

# default values
print(my_inst_1.metadata.system.height)  # Output: None (default value not set yet)

my_inst_1.metadata.system.height = 100  # Setting default value for metadata.system.height
print(my_inst_1.to_dict()['metadata']['system']['height'])  # Output: 100

# autocomplete - should complete to metadata
print(my_inst_1.metadata)  # Output: {'system': {'size': 10.7, 'height': 100}, 'user': {'batch': 10}}
