from db.run_sql import run_sql
from models.transaction import Transaction

def save(transaction):
    sql = "INSERT INTO transactions (user_id, date, value, description, merchant_id, priority) VALUES (%s, %s, %s, %s, %s, %s) RETURNING ID"
    values = [transaction.user.id, transaction.date, transaction.value, transaction.description, transaction.merchant.id, transaction.priority_rating]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)