from datetime import datetime

class Transaction:

    def __init__(self, user, value, description, id=None):
        
        self.user = user
        self.value = value
        self.description = description
        self.date = None
        self.merchant = None
        self.priority_rating = None
        self.id = id
        self.tag = None
    
    def set_priority_rating(self, rating):
        try:
            rating = int(rating)
            if 0 <= rating <= 3:
                self.priority_rating = self.priority_list[rating]
            else:
                return "Please enter value between 0 and 3"
        except:
            return "Please enter value between 0 and 3"

class DirectDebit(Transaction):

    #init that extends parent class init and adds own attributes
    def __init__(self, *args, **kwargs):        
        #function that facilitates extention of init from parent class
        super(DirectDebit, self).__init__(*args, **kwargs)
        #how many times in said duration
        self.reoccurence_frequency_amount = None
        #type of said duration
        self.reoccurence_frequency_type = None
        #said duration type list
        self.reoccurence_frequency_type_list = ["day", "week", "year"] 
        self.reoccurence_frequency_type_amount= None
        #picture to highlight it's a direct debit
        self.icon = "Test"

class Debt(DirectDebit):
    def __init__(self, *args, **kwargs):        
        #function that facilitates extention of init from parent class
        super(Debt, self).__init__(*args, **kwargs)  
        # self.interest = None
        self.late_payment_fine = None
        self.pay_off_date = None 
    
    def calculate_time_left(self, date_1, date_2):
        date_1 = datetime.strptime(date_1, "%Y-%m-%d")
        date_2 = datetime.strptime(date_2, "%Y-%m-%d")
        return abs((date_2 - date_1).days)