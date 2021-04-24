import pdb
from models.user import User
from models.extras import *

import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository

user_repository.delete_all()
merchant_repository.delete_all()

user_1 = User('John', 'Doe', 20)
user_1.budget = 100
user_repository.save(user_1)

user_2 = User('Steve', 'Smith', 15)
user_2.budget = 10
user_2.dark_mode = True
user_repository.save(user_2)

user_3 = User('Kylie', 'Evans', 50)
user_3.budget = 1000
user_3.dark_mode = True
user_repository.save(user_3)

merchant_1 = Merchant('Amazon')
merchant_1.icon = 'Piccy'
merchant_1.website = 'https//:www.amazon.co.uk'
merchant_repository.save(merchant_1)

merchant_2 = Merchant('Ebay')
merchant_2.icon = 'Piccy'
merchant_2.website = 'https//:www.ebay.co.uk'
merchant_repository.save(merchant_2)

merchant_3 = Merchant('Asos')
merchant_3.icon = 'Piccy'
merchant_3.website = 'https//:www.asos.co.uk'
merchant_repository.save(merchant_3)