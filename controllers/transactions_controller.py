from app import app
from flask import render_template, request, redirect, url_for
from flask import Blueprint
from session import session
from models.transaction import *
import repositories.user_repository as user_repository
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository



transactions_blueprint = Blueprint('transactions', __name__)
@transactions_blueprint.route('/transactions')
def transactions():
    user = user_repository.select(session)
    budget = user.budget
    return render_template('transactions/transactions.html', budget= budget)

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

@transactions_blueprint.route('/add_direct_debit')
def add_direct_debit():
    return render_template('transactions/add_direct_debit.html')

@transactions_blueprint.route('/add_debt')
def add_debt():
    return render_template('transactions/add_debt.html')

@transactions_blueprint.route('/add_custom_tag')
def add_custom_tag():
    return render_template('transactions/extras/add_custom_tag.html')

@transactions_blueprint.route('/add_merchant')
def add_merchant():
    return render_template('transactions/extras/add_merchant.html')