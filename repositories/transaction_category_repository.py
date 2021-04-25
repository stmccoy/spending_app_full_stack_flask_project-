from db.run_sql import run_sql
from models.transaction_category import TransactionCategory
import repositories.transaction_repository as transaction_repository
import repositories.direct_debit_repository as direct_debit_repository
import repositories.debt_repository as debt_repository
import repositories.tag_repository as tag_repository

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

def select(id):
    transaction_category = None
    sql = "SELECT * FROM transaction_categories WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:

        # transaction = transaction_repository.select(result['transaction_id'])
        # direct_debit = direct_debit_repository.select(result['direct_debit_id'])
        # if result['debt_id']:
        tag = tag_repository.select(result['tag_id'])
        transaction_category = TransactionCategory(tag, result['id'])   
        if result['debt_id'] != None:
            debt = debt_repository.select(result['debt_id'])
            transaction_category.debt = debt
        elif result['transaction_id'] != None:
            transaction = transaction_repository.select(result['transaction_id'])
            transaction_category.transaction = transaction
        elif result['direct_debit_id'] != None:
            direct_debit = direct_debit_repository.select(result['direct_debit_id'])  
            transaction_category.direct_debit = direct_debit
    return transaction_category