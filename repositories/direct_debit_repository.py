from db.run_sql import run_sql
from models.transaction import DirectDebit

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