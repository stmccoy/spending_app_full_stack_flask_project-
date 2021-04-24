import pdb
from models.user import User
from models.extras import *
from models.transaction import *
from models.frequent_trades import FrequentTrade
from models.transaction_category import TransactionCategory

import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.direct_debit_repository as direct_debit_repository
import repositories.debt_repository as debt_repository
import repositories.tag_repository as tag_repository
import repositories.frequent_trade_repository as frequent_trade_repository
import repositories.transaction_category_repository as transaction_category_repository

user_repository.delete_all()
merchant_repository.delete_all()
transaction_repository.delete_all()
direct_debit_repository.delete_all()
debt_repository.delete_all()
tag_repository.delete_all()
frequent_trade_repository.delete_all()
transaction_category_repository.delete_all()

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

tag_1 = Tag('Food')
tag_repository.save(tag_1)

tag_2 = Tag('Gambling', True)
tag_repository.save(tag_2)

transaction_1 = Transaction(user_1, 20, "shoes")
transaction_1.merchant = merchant_1
transaction_1.priority_rating = 0
transaction_repository.save(transaction_1)

transaction_2 = Transaction(user_2, 20, "hairclips")
transaction_2.merchant = merchant_2
transaction_2.priority_rating = 1
transaction_repository.save(transaction_2)

transaction_3 = Transaction(user_3, 20, "socks")
transaction_3.merchant = merchant_3
transaction_3.priority_rating = 1
transaction_repository.save(transaction_3)

merchant_4 = Merchant("The Gym Group")
merchant_4.icon = 'Piccy'
merchant_4.website = "https//www.thegym.com"
merchant_repository.save(merchant_4)

merchant_5 = Merchant("Samsung")
merchant_5.icon = 'Piccy'
merchant_5.website = "https//www.samsung.com"
merchant_repository.save(merchant_5)

merchant_6 = Merchant("Ford Motors")
merchant_6.icon = 'Piccy'
merchant_6.website = "https//www.ford.com"
merchant_repository.save(merchant_6)

direct_debit_1 = DirectDebit(user_1, 20, "Gym")
direct_debit_1.merchant = merchant_4
direct_debit_1.priority_rating = 2
direct_debit_1.reoccurence_frequency_amount = 1
direct_debit_1.reoccurence_frequency_type = 2
direct_debit_1.reoccurence_frequency_type_amount = 3
direct_debit_1.icon = "Piccy"
direct_debit_repository.save(direct_debit_1)

direct_debit_2 = Transaction(user_2, 30, "Phone")
direct_debit_2.merchant = merchant_5
direct_debit_2.priority_rating = 2
direct_debit_2.reoccurence_frequency_amount = 2
direct_debit_2.reoccurence_frequency_type = 1
direct_debit_2.reoccurence_frequency_type_amount = 3
direct_debit_2.icon = "Piccy"
direct_debit_repository.save(direct_debit_2)

direct_debit_3 = Transaction(user_3, 100, "Car")
direct_debit_3.merchant = merchant_6
direct_debit_3.priority_rating = 3
direct_debit_3.reoccurence_frequency_amount = 1
direct_debit_3.reoccurence_frequency_type = 3
direct_debit_3.reoccurence_frequency_type_amount = 2
direct_debit_3.icon = "Piccy"
direct_debit_repository.save(direct_debit_3)

merchant_7 = Merchant("Barclays")
merchant_7.icon = 'Piccy'
merchant_7.website = "https//www.barclaysbank.com"
merchant_repository.save(merchant_7)

merchant_8 = Merchant("HMRC")
merchant_8.icon = 'Piccy'
merchant_8.website = "https//www.gov.uk"
merchant_repository.save(merchant_8)

merchant_9 = Merchant("HSBC")
merchant_9.icon = 'Piccy'
merchant_9.website = "https//www.hsbc.com"
merchant_repository.save(merchant_9)

debt_1 = Debt(user_1, 200, "Mortgage")
debt_1.merchant = merchant_7
debt_1.priority_rating = 4
debt_1.reoccurence_frequency_amount = 1
debt_1.reoccurence_frequency_type = 2
debt_1.reoccurence_frequency_type_amount = 1
debt_1.icon = "Piccy"
debt_1.interest = 2
debt_1.late_payment_fine = 10
debt_1.pay_off_date = "2022-02-12"
debt_repository.save(debt_1)

debt_2 = Debt(user_2, 100, "Tax debt")
debt_2.merchant = merchant_8
debt_2.priority_rating = 4
debt_2.reoccurence_frequency_amount = 1
debt_2.reoccurence_frequency_type = 2
debt_2.reoccurence_frequency_type_amount = 2
debt_2.icon = "Piccy"
debt_2.interest = 0
debt_2.late_payment_fine = 50
debt_2.pay_off_date = "2023-06-12"
debt_repository.save(debt_2)

debt_3 = Debt(user_2, 100, "Credit Card Debt")
debt_3.merchant = merchant_9
debt_3.priority_rating = 3
debt_3.reoccurence_frequency_amount = 2
debt_3.reoccurence_frequency_type = 1
debt_3.reoccurence_frequency_type_amount = 1
debt_3.icon = "Piccy"
debt_3.interest = 10
debt_3.late_payment_fine = 40
debt_3.pay_off_date = "2021-11-12"
debt_repository.save(debt_3)

frequent_trade_1 = FrequentTrade(user_1, merchant_4)
frequent_trade_repository.save(frequent_trade_1)

frequent_trade_2 = FrequentTrade(user_2, merchant_7)
frequent_trade_repository.save(frequent_trade_2)

frequent_trade_3 = FrequentTrade(user_3, merchant_9)
frequent_trade_repository.save(frequent_trade_3)

transaction_category_1 = TransactionCategory(transaction_1, direct_debit_1, debt_1, tag_1)
transaction_category_repository.save(transaction_category_1)

transaction_category_2 = TransactionCategory(transaction_2, direct_debit_2, debt_2, tag_2)
transaction_category_repository.save(transaction_category_2)

transaction_category_3 = TransactionCategory(transaction_3, direct_debit_3, debt_3, tag_1)
transaction_category_repository.save(transaction_category_3)
