class FrozenMatrix:
    def __init__(self, rows):
        # каждая строка -> вложенный кортеж
        self._data = tuple(tuple(row) for row in rows)

    def __getitem__(self, idx):
        #  строка по индексу
        return self._data[idx]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __eq__(self, other):
        if not isinstance(other, FrozenMatrix):
            return False
        return self._data == other._data

    def __hash__(self):
        return hash(self._data)

    def __repr__(self):
        return f"FrozenMatrix({self._data})"
