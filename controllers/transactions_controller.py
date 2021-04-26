from app import app
from flask import render_template, request, redirect, url_for
from flask import Blueprint
from session import session
from models.transaction import *
from models.extras import *
import repositories.user_repository as user_repository
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.direct_debit_repository as direct_debit_repository
import repositories.debt_repository as debt_repository
import repositories.tag_repository as tag_repository



transactions_blueprint = Blueprint('transactions', __name__)
@transactions_blueprint.route('/transactions')
def transactions():
    user = user_repository.select(session)
    budget = user.budget
    transactions = transaction_repository.select_by_user(str(user.id))
    direct_debits = direct_debit_repository.select_by_user(str(user.id))
    debts = debt_repository.select_by_user(str(user.id))
    return render_template('transactions/transactions.html', budget= budget, transactions=transactions, direct_debits=direct_debits, debts= debts)

@transactions_blueprint.route('/set_budget', methods=['GET', 'POST'])
def set_budget():
    if request.method == 'POST':
        budget = request.form['budget']
        user_repository.update_user_budget(budget, session)  
        return redirect(url_for('transactions.transactions'))
    return render_template('transactions/set_budget.html')

@transactions_blueprint.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    if request.method == "POST":
        user = user_repository.select(session)
        value = request.form['value']
        description = request.form['description']
        transaction = Transaction(user, value, description)
        transaction.date = request.form['date']
        transaction.priority_rating = request.form['priority_rating']
        merchant_name = request.form['merchant']
        #if statement for if merchant = [] do add merchant method else do below
        merchant = merchant_repository.select_by_name(merchant_name)[0]
        transaction.merchant = merchant
        transaction_repository.save(transaction)
        return redirect(url_for('transactions.transactions'))
    return render_template('transactions/add_transaction.html')

@transactions_blueprint.route('/add_direct_debit', methods=['GET', 'POST'])
def add_direct_debit():
    if request.method == "POST":
        user = user_repository.select(session)
        value = request.form['value']
        description = request.form['description']
        direct_debit = DirectDebit(user, value, description)
        direct_debit.date = request.form['date']
        direct_debit.priority_rating = request.form['priority_rating']
        merchant_name = request.form['merchant']
        #if statement for if merchant = [] do add merchant method else do below
        merchant = merchant_repository.select_by_name(merchant_name)[0]
        direct_debit.merchant = merchant
        direct_debit.reoccurence_frequency_amount = request.form['reoccurence_frequency_amount']
        direct_debit_repository.save(direct_debit)
        #need to fix table to allow for string and add freq amount type 
        return redirect(url_for('transactions.transactions'))
    return render_template('transactions/add_direct_debit.html')

@transactions_blueprint.route('/add_debt', methods=['GET', 'POST'])
def add_debt():
    if request.method == "POST":
        user = user_repository.select(session)
        value = request.form['value']
        description = request.form['description']
        debt = Debt(user, value, description)
        debt.date = request.form['date']
        debt.priority_rating = request.form['priority_rating']
        merchant_name = request.form['merchant']
        #if statement for if merchant = [] do add merchant method else do below
        merchant = merchant_repository.select_by_name(merchant_name)[0]
        debt.merchant = merchant
        debt.reoccurence_frequency_amount = request.form['reoccurence_frequency_amount']
        debt.interest = request.form['interest']
        debt.late_payment_fine = request.form['late_payment_fine']
        debt.pay_off_date = request.form['pay_off_date']
        debt_repository.save(debt)
        #need to fix table to allow for string and add freq amount type 
        return redirect(url_for('transactions.transactions'))
    return render_template('transactions/add_debt.html')

@transactions_blueprint.route('/add_custom_tag', methods=['GET', 'POST'])
def add_custom_tag():
    if request.method == 'POST':
        tag_name = request.form['tag_name']
        tag = Tag(tag_name)
        if 'adult_rating' in request.form:
            tag = Tag(tag_name, True)
        tag_repository.save(tag)
        return redirect(url_for('transactions.transactions'))
    return render_template('transactions/extras/add_custom_tag.html')

# @transactions_blueprint.route('/add_merchant')
# def add_merchant():
#     return render_template('transactions/extras/add_merchant.html')