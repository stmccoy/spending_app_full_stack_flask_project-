from db.run_sql import run_sql
from models.transaction_category import TransactionCategory

def save_transaction_category(transaction_category):
    sql = "INSERT INTO transaction_categories (transaction_id, tag_id) VALUES (%s, %s) RETURNING ID"
    values = [transaction_category.transaction.id, transaction_category.tag.id]
    results = run_sql( sql, values )
    transaction_category.id = results[0]['id']
    return transaction_category

def save_direct_debit_category(transaction_category):
    sql = "INSERT INTO transaction_categories (direct_debit_id, tag_id) VALUES (%s, %s) RETURNING ID"
    values = [transaction_category.direct_debit.id, transaction_category.tag.id]
    results = run_sql( sql, values )
    transaction_category.id = results[0]['id']
    return transaction_category

def save_debt_category(transaction_category):
    sql = "INSERT INTO transaction_categories (debt_id, tag_id) VALUES (%s, %s) RETURNING ID"
    values = [transaction_category.debt.id, transaction_category.tag.id]
    results = run_sql( sql, values )
    transaction_category.id = results[0]['id']
    return transaction_category

def delete_all():
    sql = "DELETE FROM transaction_categories"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transaction_categories WHERE id = %s"
    values = [id]
    run_sql(sql, values)