from collections import namedtuple
from datetime import datetime

Transaction = namedtuple(
    "Transaction", "giver points date", defaults=(None, None, datetime.now())
)


class User:
    def __init__(self, name):
        self.name = name
        self._transactions = []

    def __add__(self, other):
        self._transactions.append(other)

    @property
    def karma(self):
        return sum(t.points for t in self._transactions)

    @property
    def points(self):
        return [t.points for t in self._transactions]

    @property
    def fans(self):
        return len(set(t.giver for t in self._transactions))

    def __str__(self):
        if self.fans == 1:
            return f"{self.name} has a karma of {self.karma} and {self.fans} fan"
        return f"{self.name} has a karma of {self.karma} and {self.fans} fans"
