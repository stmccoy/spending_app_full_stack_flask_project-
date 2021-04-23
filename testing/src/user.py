class User:

    def __init__(self, first_name, surname, age):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.favourite_merchants = []
        self.budget = None
        self.transactions = []
        self.direct_debits = []
        self.dark_mode = False
        self.debts=[]

