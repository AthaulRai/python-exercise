class DataNode:
    def __init__(self, data=None):
        self._data = data if data is not None else {}

    def __getattr__(self, item):
        if item in self._data:
            value = self._data[item]
            if isinstance(value, dict):
                return DataNode(value)
            return value
        return None

    def __setattr__(self, key, value):
        if key != "_data":
            self._data[key] = value
        else:
            self.__dict__[key] = value

    def __delattr__(self, item):
        if item in self._data:
            del self._data[item]

    def __getitem__(self, item):
        if item in self._data:
            value = self._data[item]
            if isinstance(value, dict):
                return DataNode(value)
            return value
        raise KeyError(f"'{item}' not found in DataNode object.")

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, item):
        if item in self._data:
            del self._data[item]

    def to_dict(self):
        return self._data


class Data:
    def __init__(self, **kwargs):
        self._data = kwargs.get("data", {})
        self._default_values = kwargs.get("default_values", {})

    @classmethod
    def from_dict(cls, data):
        return cls(data=data)

    def __getattr__(self, item):
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
            return self.__dict__[item]

    def __setattr__(self, key, value):
        if key in ["_data", "_default_values"]:
            self.__dict__[key] = value
        else:
            self._data[key] = value

    def __delattr__(self, item):
        if item in self._data:
            del self._data[item]

    def __getitem__(self, item):
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
        self._data[key] = value

    def __delitem__(self, item):
        if item in self._data:
            del self._data[item]

    def to_dict(self):
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

