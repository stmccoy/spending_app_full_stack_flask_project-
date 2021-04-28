from db.run_sql import run_sql
from models.frequent_trades import FrequentTrade
from models.extras import Merchant
import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository

def delete_all():
    sql = "DELETE FROM frequent_trades"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM frequent_trades WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select(id):
    frequent_trade = None
    sql = "SELECT * FROM frequent_trades WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = user_repository.select(result['user_id'])
        merchant = merchant_repository.select(result['merchant_id'])
        frequent_trade = FrequentTrade(user, merchant, result['id'])
    return frequent_trade

def select_all():
    frequent_trades = []

    sql = "SELECT * FROM frequent_trades"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        frequent_trade = FrequentTrade(user, merchant, row['id'])
        frequent_trades.append(frequent_trade)
    return frequent_trades

def select_all_by_user(user_id):
    merchants = []

    sql = "SELECT * FROM frequent_trades INNER JOIN merchants ON merchants.id = frequent_trades.merchant_id WHERE user_id = %s"
    values = [user_id]
    results = run_sql(sql, values)

    for row in results:
        merchant_name = row['merchant_name']
        merchant_icon = row['icon']
        merchant_website = row['website']
        merchant_id = row['merchant_id']
        merchant = Merchant(merchant_name, merchant_id)
        merchant.website = merchant_website
        merchant.icon = merchant_icon
        merchants.append(merchant)

    return merchants

##
# def select_all_by_user_and_merchant(user_id, merchant_id):
#     merchants = []

#     sql = "SELECT * FROM frequent_trades INNER JOIN merchants ON merchants.id = frequent_trades.merchant_id WHERE user_id = %s AND merchant_id = %s"
#     values = [user_id, merchant_id]
#     results = run_sql(sql, values)

#     for row in results:
#         merchant_name = row['merchant_name']
#         merchant_icon = row['icon']
#         merchant_website = row['website']
#         merchant = Merchant(merchant_name)
#         merchant.website = merchant_website
#         merchant.icon = merchant_icon
#         merchants.append(merchant)

#     return merchants


def save(frequent_trade):
    if select_all_by_user_and_merchant(frequent_trade.user.id, frequent_trade.merchant.id) != []:
        return False
    sql = "INSERT INTO frequent_trades (user_id, merchant_id) VALUES (%s, %s) RETURNING ID"
    values = [frequent_trade.user.id, frequent_trade.merchant.id]
    results = run_sql( sql, values )
    frequent_trade.id = results[0]['id']
    return frequent_trade