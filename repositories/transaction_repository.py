from db.run_sql import run_sql
from models.transaction import Transaction
from models.frequent_trades import FrequentTrade
import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository
import repositories.frequent_trade_repository as frequent_trade_repository
import repositories.tag_repository as tag_repository


def save(transaction):
    transaction_merchant_data = None
    transaction_tag_data = None
    sql = "INSERT INTO transactions (user_id, date, value, description, merchant_id, priority, tag_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING ID"
    if transaction.merchant:
        transaction_merchant_data = transaction.merchant.id
        frequent_trade = FrequentTrade(transaction.user, transaction.merchant)
        frequent_trade_repository.save(frequent_trade)
    if transaction.tag:
        transaction_tag_data = transaction.tag.id
    values = [transaction.user.id, transaction.date, transaction.value, transaction.description, transaction_merchant_data, transaction.priority_rating, transaction_tag_data]#needs to be id for tag
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
        if tag_repository.select(result['tag_id']) is None:
            tag = None
        else:
            tag = tag_repository.select(result['tag_id'])
        transaction = Transaction(user, result['value'], result['description'], result['id'])
        transaction.date = result['date']
        transaction.merchant = merchant
        transaction.tag = tag
        transaction.priority_rating = result['priority']
    return transaction

def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        tag = tag_repository.select(row['tag_id'])
        transaction = Transaction(user, row['value'], row['description'], row['id'])
        transaction.date = row['date']
        transaction.merchant = merchant
        transaction.tag = tag
        transaction.priority_rating = row['priority']
        transactions.append(transaction)
    return transactions

def select_by_description(description):
    transactions = []

    sql = "SELECT * FROM transactions WHERE description = %s"
    values = [name]
    results = run_sql(sql, values)

    for row in results:
        user = user_repository.select(row['user_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        tag = tag_repository.select(row['tag_id'])
        transaction = Transaction(user, row['value'], row['description'], row['id'])
        transaction.date = row['date']
        transaction.merchant = merchant
        transaction.tag = tag
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
        tag = tag_repository.select(row['tag_id'])
        transaction = Transaction(user, row['value'], row['description'], row['id'])
        transaction.date = row['date']
        transaction.merchant = merchant
        transaction.tag = tag
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
        tag = tag_repository.select(row['tag_id'])
        transaction = Transaction(user, row['value'], row['description'], row['id'])
        transaction.date = row['date']
        transaction.merchant = merchant
        transaction.tag = tag
        transaction.priority_rating = row['priority']
        transactions.append(transaction)
    return transactions

def update(transaction):
    transaction_merchant_data = None
    transaction_tag_data = None
    sql = "UPDATE transactions SET (date, value, description, merchant_id, priority, tag_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    if transaction.merchant:
        transaction_merchant_data = transaction.merchant.id
        frequent_trade = FrequentTrade(transaction.user, transaction.merchant)
        frequent_trade_repository.save(frequent_trade)
    if transaction.tag:
        transaction_tag_data = transaction.tag.id
    values = [transaction.date, transaction.value, transaction.description, transaction_merchant_data, transaction.priority_rating, transaction_tag_data, transaction.id]
    run_sql(sql, values)