class Merchant:

    def __init__(self, name):
        self.name = name
        self.icon = None
        self.website = None

class Tag:

    def __init__(self, name, adult_rating=False):
        self.name = name
        self.adult_rating = adult_rating