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
    
    def change_theme(self):
        if self.dark_mode:
            self.dark_mode = False
        else:
            self.dark_mode=True
    
    def age_suitability(self, tag_object):
        if tag_object.adult_rating and self.age < 18:
            return False
        return True

