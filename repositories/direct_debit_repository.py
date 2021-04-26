from db.run_sql import run_sql
from models.transaction import DirectDebit
import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository

def save(direct_debit):
    sql = "INSERT INTO direct_debits (user_id, date, value, description, merchant_id, priority, reoccurence_frequency_amount, reoccurence_frequency_type, reoccurence_frequency_type_amount, icon) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s) RETURNING ID"
    values = [direct_debit.user.id, direct_debit.date, direct_debit.value, direct_debit.description, direct_debit.merchant.id, direct_debit.priority_rating, direct_debit.reoccurence_frequency_amount, direct_debit.reoccurence_frequency_type, direct_debit.reoccurence_frequency_type_amount, direct_debit.icon]
    results = run_sql(sql, values)
    direct_debit.id = results[0]['id']
    return direct_debit

def delete_all():
    sql = "DELETE FROM direct_debits"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM direct_debits WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select(id):
    direct_debit = None
    sql = "SELECT * FROM direct_debits WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = user_repository.select(result['user_id'])
        merchant = merchant_repository.select(result['merchant_id'])
        direct_debit = DirectDebit(user, result['value'], result['description'], result['id'])
        direct_debit.date = result['date']
        direct_debit.merchant = merchant
        direct_debit.priority_rating = result['priority']
        direct_debit.reoccurence_frequency_amount = result['reoccurence_frequency_amount']
        direct_debit.reoccurence_frequency_type = result['reoccurence_frequency_type']
        direct_debit.reoccurence_frequency_type_amount = result['reoccurence_frequency_type_amount']
        direct_debit.icon = result['icon']
    return direct_debit

def select_all():
    direct_debits = []

    sql = "SELECT * FROM direct_debits"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        direct_debit = DirectDebit(user, row['value'], row['description'], row['id'])
        direct_debit.date = row['date']
        direct_debit.merchant = merchant
        direct_debit.priority_rating = row['priority']
        direct_debit.reoccurence_frequency_amount = row['reoccurence_frequency_amount']
        direct_debit.reoccurence_frequency_type = row['reoccurence_frequency_type']
        direct_debit.reoccurence_frequency_type_amount = row['reoccurence_frequency_type_amount']
        direct_debit.icon = row['icon']
        direct_debits.append(direct_debit)
    return direct_debits

def select_by_user(user_id):
    direct_debits = []
    sql = "SELECT * FROM direct_debits INNER JOIN merchants ON merchants.id = direct_debits.merchant_id WHERE user_id = %s"
    values = [user_id]
    results = run_sql(sql, values)

    for row in results:
        user = user_repository.select(row['user_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        direct_debit = DirectDebit(user, row['value'], row['description'], row['id'])
        direct_debit.date = row['date']
        direct_debit.merchant = merchant
        direct_debit.priority_rating = row['priority']
        direct_debit.priority_rating = row['priority']
        direct_debit.reoccurence_frequency_amount = row['reoccurence_frequency_amount']
        direct_debit.reoccurence_frequency_type = row['reoccurence_frequency_type']
        direct_debit.reoccurence_frequency_type_amount = row['reoccurence_frequency_type_amount']
        direct_debit.icon = row['icon']
        direct_debits.append(direct_debit)
    return direct_debits