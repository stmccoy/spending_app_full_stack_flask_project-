from db.run_sql import run_sql
from models.transaction import Transaction
import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository

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

def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = user_repository.select(result['user_id'])
        merchant = merchant_repository.select(result['merchant_id'])
        transaction = Transaction(user, result['value'], result['description'], result['id'])
        transaction.date = result['date']
        transaction.merchant = merchant
        transaction.priority_rating = result['priority']
    return transaction