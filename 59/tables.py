class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
        their calculations (form of caching)"""
        self._table = [[] for _ in range(length)]
        for i in range(length):
            for j in range(length):
                self._table[i].append((i + 1) * (j + 1))

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self._table) * len(self._table[0])

    def __str__(self):
        """Returns a string representation of the table"""
        table_str = []
        for row in self._table:
            table_str.append(" | ".join(str(cell) for cell in row))
        return "\n".join(table_str)

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        try:
            return self._table[x - 1][y - 1]
        except IndexError as e:
            raise IndexError(e)
