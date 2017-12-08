command_list = []


class Command:
    def __init__(self):
        self._keys = []
        self.description = ''
        command_list.append(self)

    @property
    def keys(self):
        return self._keys

    @keys.setter
    def keys(self, value):
        self._keys = value

    def handle(self):
        pass
