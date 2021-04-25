from app import app
from flask import render_template, request, redirect, url_for
from flask import Blueprint
from session import session
import repositories.user_repository as user_repository

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

@transactions_blueprint.route('/add_transaction')
def add_transaction():
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