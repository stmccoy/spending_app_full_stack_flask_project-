from db.run_sql import run_sql
from models.transaction import Debt

def save(debt):
    sql = "INSERT INTO debts (user_id, date, value, description, merchant_id, priority, reoccurence_frequency_amount, reoccurence_frequency_type, reoccurence_frequency_type_amount, icon, interest, late_payment_fine, pay_off_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING ID"
    values = [debt.user.id, debt.date, debt.value, debt.description, debt.merchant.id, debt.priority_rating, debt.reoccurence_frequency_amount, debt.reoccurence_frequency_type, debt.reoccurence_frequency_type_amount, debt.icon, debt.interest, debt.late_payment_fine, debt.pay_off_date]
    results = run_sql(sql, values)
    debt.id = results[0]['id']
    return debt

def delete_all():
    sql = "DELETE FROM direct_debits"
    run_sql(sql)