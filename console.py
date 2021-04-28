from models.user import User
from models.extras import *
from models.transaction import *
from models.frequent_trades import FrequentTrade

import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.direct_debit_repository as direct_debit_repository
import repositories.debt_repository as debt_repository
import repositories.tag_repository as tag_repository
import repositories.frequent_trade_repository as frequent_trade_repository

user_repository.delete_all()
merchant_repository.delete_all()
transaction_repository.delete_all()
direct_debit_repository.delete_all()
debt_repository.delete_all()
tag_repository.delete_all()
frequent_trade_repository.delete_all()

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

merchant = Merchant('None')
merchant.website = 'None'
merchant_repository.save(merchant)

merchant_1 = Merchant('Amazon')
merchant_1.website = 'https//:www.amazon.co.uk'
merchant_repository.save(merchant_1)

merchant_2 = Merchant('Ebay')
merchant_2.website = 'https//:www.ebay.co.uk'
merchant_repository.save(merchant_2)

merchant_3 = Merchant('Asos')
merchant_3.website = 'https//:www.asos.co.uk'
merchant_repository.save(merchant_3)

merchant_4 = Merchant("The Gym Group")
merchant_4.website = "https//www.thegym.com"
merchant_repository.save(merchant_4)

merchant_5 = Merchant("Samsung")
merchant_5.website = "https//www.samsung.com"
merchant_repository.save(merchant_5)

merchant_6 = Merchant("Ford Motors")
merchant_6.website = "https//www.ford.com"
merchant_repository.save(merchant_6)

merchant_7 = Merchant("Barclays")
merchant_7.website = "https//www.barclaysbank.com"
merchant_repository.save(merchant_7)

merchant_8 = Merchant("HMRC")
merchant_8.website = "https//www.gov.uk"
merchant_repository.save(merchant_8)

merchant_9 = Merchant("HSBC")
merchant_9.website = "https//www.hsbc.com"
merchant_repository.save(merchant_9)

merchant_10 = Merchant("Gamesmaster")
merchant_10.website = "https//www.fakewebsite.com"
merchant_repository.save(merchant_10)

merchant_11 = Merchant("Hill Dickinson")
merchant_11.website = "https://www.hilldickinson.com"
merchant_repository.save(merchant_11)

merchant_12 = Merchant("Kyle")
merchant_12.website = "https://www.instagram.com/kylesinstagram"
merchant_repository.save(merchant_12)

tag = Tag('None')
tag_repository.save(tag)

tag_1 = Tag('Clothes')
tag_repository.save(tag_1)

tag_2 = Tag('Gambling', True)
tag_repository.save(tag_2)

tag_3 = Tag('Entertainment')
tag_repository.save(tag_3)

tag_4 = Tag('hair and beauty')
tag_repository.save(tag_4)

tag_5 = Tag('sport')
tag_repository.save(tag_5)

tag_6 = Tag('fitness and health')
tag_repository.save(tag_6)

tag_7 = Tag('Utilities')
tag_repository.save(tag_7)

tag_8 = Tag('Housing')
tag_repository.save(tag_8)

tag_9 = Tag('Banking')
tag_repository.save(tag_9)

tag_10 = Tag('Tax')
tag_repository.save(tag_10)

tag_11 = Tag('Law fees')
tag_repository.save(tag_11)

transaction_1 = Transaction(user_1, 20, "shoes")
transaction_1.date = "2021-04-11"
transaction_1.merchant = merchant_3
transaction_1.priority_rating = None
transaction_1.tag = tag_1
transaction_repository.save(transaction_1)

transaction_2 = Transaction(user_2, 20, "hairclips")
transaction_2.date = "2021-03-09"
transaction_2.merchant = merchant_2
transaction_2.priority_rating = "low"
transaction_2.tag = tag_4
transaction_repository.save(transaction_2)

transaction_3 = Transaction(user_3, 20, "socks")
transaction_3.date = "2021-02-08"
transaction_3.merchant = merchant_3
transaction_3.priority_rating = None
transaction_3.tag = tag_1
transaction_repository.save(transaction_3)

transaction_4 = Transaction(user_1, 20, "dvds")
transaction_4.date = "2021-03-09"
transaction_4.merchant = merchant_1
transaction_4.priority_rating = "low"
transaction_4.tag = tag_3
transaction_repository.save(transaction_4)

transaction_5 = Transaction(user_1, 20, "perfume")
transaction_5.date = "2021-01-11"
transaction_5.merchant = merchant_2
transaction_5.priority_rating = "low"
transaction_5.tag = tag_4
transaction_repository.save(transaction_5)

transaction_6 = Transaction(user_2, 20, "football")
transaction_6.date = "2021-02-21"
transaction_6.merchant = merchant_1
transaction_6.priority_rating = "low"
transaction_6.tag = tag_5
transaction_repository.save(transaction_6)

transaction_7 = Transaction(user_3, 20, "t-shirt")
transaction_7.date = "2021-03-22"
transaction_7.merchant = merchant_2
transaction_7.priority_rating = None
transaction_7.tag = tag_1
transaction_repository.save(transaction_7)

transaction_8 = Transaction(user_1, 10, "Lost the money")
transaction_8.date = "2021-05-27"
transaction_8.merchant = merchant
transaction_8.priority_rating = None
transaction_8.tag = tag
transaction_repository.save(transaction_8)

direct_debit_1 = DirectDebit(user_1, 20, "Gym")
direct_debit_1.date = "2021-02-07"
direct_debit_1.merchant = merchant_4
direct_debit_1.priority_rating = "medium"
direct_debit_1.reoccurence_frequency_amount = 1
direct_debit_1.reoccurence_frequency_type = 'month'
direct_debit_1.tag = tag_6
direct_debit_repository.save(direct_debit_1)

direct_debit_2 = DirectDebit(user_2, 30, "Phone")
direct_debit_2.date = "2021-05-05"
direct_debit_2.merchant = merchant_5
direct_debit_2.priority_rating = "medium"
direct_debit_2.reoccurence_frequency_amount = 1
direct_debit_2.reoccurence_frequency_type = 'month'
direct_debit_2.tag = tag_7
direct_debit_repository.save(direct_debit_2)

direct_debit_3 = DirectDebit(user_3, 100, "Car")
direct_debit_3.date = "2021-04-08"
direct_debit_3.merchant = merchant_6
direct_debit_3.priority_rating = "high"
direct_debit_3.reoccurence_frequency_amount = 1
direct_debit_3.reoccurence_frequency_type = 'week'
direct_debit_3.tag = tag_1
direct_debit_repository.save(direct_debit_3)

direct_debit_4 = DirectDebit(user_1, 100, "TV license")
direct_debit_4.date = "2021-03-21"
direct_debit_4.merchant = merchant_8
direct_debit_4.priority_rating = "medium"
direct_debit_4.reoccurence_frequency_amount = 1
direct_debit_4.reoccurence_frequency_type = 'year'
direct_debit_4.tag = tag_7
direct_debit_repository.save(direct_debit_4)

direct_debit_5 = DirectDebit(user_1, 5, "Magazine subscription")
direct_debit_5.date = "2021-04-25"
direct_debit_5.merchant = merchant_10
direct_debit_5.priority_rating = "low"
direct_debit_5.reoccurence_frequency_amount = 1
direct_debit_5.reoccurence_frequency_type = 'month'
direct_debit_5.tag = tag_7
direct_debit_repository.save(direct_debit_5)

debt_1 = Debt(user_1, 200, "Mortgage")
debt_1.date = "2022-05-11"
debt_1.merchant = merchant_7
debt_1.priority_rating = "high"
debt_1.reoccurence_frequency_amount = 1
debt_1.reoccurence_frequency_type = 'Year'
debt_1.late_payment_fine = 10
debt_1.pay_off_date = "2022-02-12"
debt_1.tag = tag_8
debt_repository.save(debt_1)

debt_2 = Debt(user_1, 100, "Tax debt")
debt_2.date = "2021-03-11"
debt_2.merchant = merchant_8
debt_2.priority_rating = "high"
debt_2.reoccurence_frequency_amount = 1
debt_2.reoccurence_frequency_type = 'Month'
debt_2.late_payment_fine = 50
debt_2.pay_off_date = "2023-06-12"
debt_2.tag = tag_10
debt_repository.save(debt_2)

debt_3 = Debt(user_3, 100, "Credit Card Debt")
debt_3.date = "2023-01-12"
debt_3.merchant = merchant_9
debt_3.priority_rating = "high"
debt_3.reoccurence_frequency_amount = 2
debt_3.reoccurence_frequency_type = 'Week'
debt_3.late_payment_fine = 40
debt_3.pay_off_date = "2021-11-12"
debt_3.tag = tag_9
debt_repository.save(debt_3)

debt_4 = Debt(user_1, 30, "lawyer fees")
debt_4.date = "2022-06-11"
debt_4.merchant = merchant_11
debt_4.priority_rating = "high"
debt_4.reoccurence_frequency_amount = 1
debt_4.reoccurence_frequency_type = 'month'
debt_4.late_payment_fine = 12
debt_4.pay_off_date = "2022-03-12"
debt_4.tag = tag_11
debt_repository.save(debt_4)

debt_5 = Debt(user_2, 20, "tic")
debt_5.date = "2022-02-10"
debt_5.merchant = merchant_12
debt_5.priority_rating = "high"
debt_5.reoccurence_frequency_amount = 1
debt_5.reoccurence_frequency_type = 'month'
debt_5.late_payment_fine = 12
debt_5.pay_off_date = "2022-11-12"
debt_5.tag = tag_11
debt_repository.save(debt_5)

frequent_trade_1 = FrequentTrade(user_1, merchant_4)
frequent_trade_repository.save(frequent_trade_1)

frequent_trade_2 = FrequentTrade(user_2, merchant_7)
frequent_trade_repository.save(frequent_trade_2)

frequent_trade_3 = FrequentTrade(user_3, merchant_9)
frequent_trade_repository.save(frequent_trade_3)
