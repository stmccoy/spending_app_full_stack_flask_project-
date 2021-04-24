class User:

#deleted self.favourite_merchants, self.debts=[], self.transactions = [] self.direct_debits = [] as they're done on another table, deleted
    def __init__(self, first_name, surname, age, id=None):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.budget = None
        self.dark_mode = False
        self.id=id
         
    def change_theme(self):
        if self.dark_mode:
            self.dark_mode = False
        else:
            self.dark_mode=True
    
    def age_suitability(self, tag_object):
        if tag_object.adult_rating and self.age < 18:
            return False
        return True

