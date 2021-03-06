from db.run_sql import run_sql
from models.transaction import Debt
from models.frequent_trades import FrequentTrade
import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository
import repositories.frequent_trade_repository as frequent_trade_repository
import repositories.tag_repository as tag_repository


def save(debt):
    debt_merchant_data = None
    debt_tag_data = None
    sql = "INSERT INTO debts (user_id, date, value, description, merchant_id, priority, tag_id,reoccurence_frequency_amount, reoccurence_frequency_type, late_payment_fine, pay_off_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING ID"
    if debt.merchant:
        debt_merchant_data = debt.merchant.id
        frequent_trade = FrequentTrade(debt.user, debt.merchant)
        frequent_trade_repository.save(frequent_trade)
    if debt.tag:
        debt_tag_data = debt.tag.id
    values = [debt.user.id, debt.date, debt.value, debt.description, debt_merchant_data, debt.priority_rating, debt_tag_data, debt.reoccurence_frequency_amount, debt.reoccurence_frequency_type, debt.late_payment_fine, debt.pay_off_date]
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
        tag = tag_repository.select(result['tag_id'])
        debt = Debt(user, result['value'], result['description'], result['id'])
        debt.date = result['date']
        debt.merchant = merchant
        debt.tag = tag
        debt.priority_rating = result['priority']
        debt.reoccurence_frequency_amount = result['reoccurence_frequency_amount']
        debt.reoccurence_frequency_type = result['reoccurence_frequency_type']
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
        tag = tag_repository.select(row['tag_id'])
        debt = Debt(user, row['value'], row['description'], row['id'])
        debt.date = row['date']
        debt.merchant = merchant
        debt.tag = tag
        debt.priority_rating = row['priority']
        debt.reoccurence_frequency_amount = row['reoccurence_frequency_amount']
        debt.reoccurence_frequency_type = row['reoccurence_frequency_type']
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
        tag = tag_repository.select(row['tag_id'])
        debt = Debt(user, row['value'], row['description'], row['id'])
        debt.date = row['date']
        debt.merchant = merchant
        debt.tag = tag
        debt.priority_rating = row['priority']
        debt.priority_rating = row['priority']
        debt.reoccurence_frequency_amount = row['reoccurence_frequency_amount']
        debt.reoccurence_frequency_type = row['reoccurence_frequency_type']
        debt.late_payment_fine = row['late_payment_fine']
        debt.pay_off_date = row['pay_off_date']
        debts.append(debt)
    return debts

def update(debt):
    debt_merchant_data = None
    debt_tag_data = None
    sql = "UPDATE debts SET (date, value, description, merchant_id, priority, tag_id, reoccurence_frequency_amount, reoccurence_frequency_type, late_payment_fine, pay_off_date) = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    if debt.merchant:
        debt_merchant_data = debt.merchant.id
    if debt.tag:
        debt_tag_data = debt.tag.id
    values = [debt.date, debt.value, debt.description, debt_merchant_data, debt.priority_rating, debt_tag_data, debt.reoccurence_frequency_amount, debt.reoccurence_frequency_type, debt.late_payment_fine, debt.pay_off_date, debt.id]
    run_sql(sql, values)