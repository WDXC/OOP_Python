class Color:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name

    """
    def set_name(self, name):
        self._name = name
    """
    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)

"""
c = Color("#ff0000", "bright red")
print(c.get_name())

c.set_name('red')
print(c.get_name())
"""

c = Color("#ff0000", "bright red")
print(c.name)

c.name = 'red'
print(c.name)

