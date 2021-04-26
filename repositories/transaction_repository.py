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

def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(user, row['value'], row['description'], row['id'])
        transaction.date = row['date']
        transaction.merchant = merchant
        transaction.priority_rating = row['priority']
        transactions.append(transaction)
    return transactions

def select_by_name(name):
    transactions = []

    sql = "SELECT * FROM transactions WHERE description = %s"
    values = [name]
    results = run_sql(sql, values)

    for row in results:
        user = user_repository.select(row['user_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(user, row['value'], row['description'], row['id'])
        transaction.date = row['date']
        transaction.merchant = merchant
        transaction.priority_rating = row['priority']
        transactions.append(transaction)
    return transactions

def select_by_merchant(merchant):
    transactions = []
    merchant_id = merchant_repository.select_by_name(merchant)[0].id
    sql = "SELECT * FROM transactions WHERE merchant_id = %s"
    values = [merchant_id]
    results = run_sql(sql, values)

    for row in results:
        user = user_repository.select(row['user_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(user, row['value'], row['description'], row['id'])
        transaction.date = row['date']
        transaction.merchant = merchant
        transaction.priority_rating = row['priority']
        transactions.append(transaction)
    return transactions

def select_by_user(user_id):
    transactions = []
    sql = "SELECT * FROM transactions WHERE user_id = %s"
    values = [user_id]
    results = run_sql(sql, values)

    for row in results:
        user = user_repository.select(row['user_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(user, row['value'], row['description'], row['id'])
        transaction.date = row['date']
        transaction.merchant = merchant
        transaction.priority_rating = row['priority']
        transactions.append(transaction)
    return transactions
