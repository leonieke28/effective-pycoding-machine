class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    def __len__(self):
        return len(self._transactions)

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __getitem__(self, position):
        return self._transactions[position]

    def __add__(self, amount):
        if not isinstance(amount, int):
            raise TypeError("The amount must be an integer!")
        self._transactions.append(amount)

    def __sub__(self, amount):
        if not isinstance(amount, int):
            raise TypeError("The amount must be an integer!")
        self._transactions.append(-amount)

    def __str__(self):
        return f"{self.name} account - balance: {self.balance}"
