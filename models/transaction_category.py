#NEEDS TESTS

class TransactionCategory:

    def __init__(self, transaction, direct_debit, debt, tag, id=None):
        self.transaction = transaction
        self.direct_debit = direct_debit
        self.debt = debt
        self.tag = tag
        self.id = id