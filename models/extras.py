class Merchant:

    def __init__(self, name, id= None):
        self.merchant_name = name
        self.icon = None
        self.website = None
        self.id = id

class Tag:

    def __init__(self, tag_name, adult_rating=False, id=None):
        self.tag_name = tag_name
        self.adult_rating = adult_rating
        self.id = id