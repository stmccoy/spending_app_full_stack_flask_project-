import pdb
from models.user import User

import repositories.user_repository as user_repository

user_repository.delete_all()

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