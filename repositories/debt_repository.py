from db.run_sql import run_sql
from models.transaction import Debt
import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository


def save(debt):
    sql = "INSERT INTO debts (user_id, date, value, description, merchant_id, priority, reoccurence_frequency_amount, reoccurence_frequency_type, reoccurence_frequency_type_amount, icon, interest, late_payment_fine, pay_off_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING ID"
    values = [debt.user.id, debt.date, debt.value, debt.description, debt.merchant.id, debt.priority_rating, debt.reoccurence_frequency_amount, debt.reoccurence_frequency_type, debt.reoccurence_frequency_type_amount, debt.icon, debt.interest, debt.late_payment_fine, debt.pay_off_date]
    results = run_sql(sql, values)
    debt.id = results[0]['id']
    return debt

def delete_all():
    sql = "DELETE FROM debts"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM debts WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select(id):
    debt = None
    sql = "SELECT * FROM debts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = user_repository.select(result['user_id'])
        merchant = merchant_repository.select(result['merchant_id'])
        debt = Debt(user, result['value'], result['description'], result['id'])
        debt.date = result['date']
        debt.merchant = merchant
        debt.priority_rating = result['priority']
        debt.reoccurence_frequency_amount = result['reoccurence_frequency_amount']
        debt.reoccurence_frequency_type = result['reoccurence_frequency_type']
        debt.reoccurence_frequency_type_amount = result['reoccurence_frequency_type_amount']
        debt.icon = result['icon']
        debt.interest = result['interest']
        debt.late_payment_fine = result['late_payment_fine']
        debt.pay_off_date = result['pay_off_date']
    return debt

def select_all():
    debts = []

    sql = "SELECT * FROM debts"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        debt = Debt(user, row['value'], row['description'], row['id'])
        debt.date = row['date']
        debt.merchant = merchant
        debt.priority_rating = row['priority']
        debt.reoccurence_frequency_amount = row['reoccurence_frequency_amount']
        debt.reoccurence_frequency_type = row['reoccurence_frequency_type']
        debt.reoccurence_frequency_type_amount = row['reoccurence_frequency_type_amount']
        debt.icon = row['icon']
        debt.interest = row['interest']
        debt.late_payment_fine = row['late_payment_fine']
        debt.pay_off_date = row['pay_off_date']
        debts.append(debt)
    return debts

def select_by_user(user_id):
    debts = []
    sql = "SELECT * FROM debts WHERE user_id = %s"
    values = [user_id]
    results = run_sql(sql, values)

    for row in results:
        user = user_repository.select(row['user_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        debt = Debt(user, row['value'], row['description'], row['id'])
        debt.date = row['date']
        debt.merchant = merchant
        debt.priority_rating = row['priority']
        debt.priority_rating = row['priority']
        debt.reoccurence_frequency_amount = row['reoccurence_frequency_amount']
        debt.reoccurence_frequency_type = row['reoccurence_frequency_type']
        debt.reoccurence_frequency_type_amount = row['reoccurence_frequency_type_amount']
        debt.icon = row['icon']
        debt.interest = row['interest']
        debt.late_payment_fine = row['late_payment_fine']
        debt.pay_off_date = row['pay_off_date']
        debts.append(debt)
    return debts