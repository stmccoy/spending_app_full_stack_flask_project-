from db.run_sql import run_sql
from models.frequent_trades import FrequentTrade

def save(frequent_trade):
    sql = "INSERT INTO frequent_trades (user_id, merchant_id) VALUES (%s, %s) RETURNING ID"
    values = [frequent_trade.user.id, frequent_trade.merchant.id]
    results = run_sql( sql, values )
    frequent_trade.id = results[0]['id']
    return frequent_trade

def delete_all():
    sql = "DELETE FROM frequent_trades"
    run_sql(sql)