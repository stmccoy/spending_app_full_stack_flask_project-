class Transaction:

    def __init__(self, value, description):
        
        self.value = value
        self.description = description
        self.merchant = None
        self.tags= []
        self.priority_list = ["low", "medium", "high"]
        self.priority_rating = None
    
    def set_priority_rating(self, rating):
        self.priority_rating = self.priority_list[rating]