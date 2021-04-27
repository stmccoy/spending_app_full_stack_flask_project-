#NEEDS TESTS

class TransactionCategory:

    def __init__(self, tag, id=None):
        self.transaction = None
        self.direct_debit = None
        self.debt = None
        self.tag = tag
        self.id = id