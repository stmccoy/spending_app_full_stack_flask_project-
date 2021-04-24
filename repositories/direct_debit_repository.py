from db.run_sql import run_sql
from models.transaction import DirectDebit

def save(direct_debit):
    sql = "INSERT INTO direct_debits (user_id, value, description, merchant, priority) VALUES (%s, %s, %s, %s, %s) RETURNING ID"
    values = [transaction.user.id, transaction.value, transaction.description, transaction.merchant.id, transaction.priority_rating]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def delete_all():
    sql = "DELETE FROM direct_debits"
    run_sql(sql)