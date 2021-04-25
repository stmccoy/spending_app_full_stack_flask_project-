from db.run_sql import run_sql
from models.frequent_trades import FrequentTrade
import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository

def save(frequent_trade):
    sql = "INSERT INTO frequent_trades (user_id, merchant_id) VALUES (%s, %s) RETURNING ID"
    values = [frequent_trade.user.id, frequent_trade.merchant.id]
    results = run_sql( sql, values )
    frequent_trade.id = results[0]['id']
    return frequent_trade

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