from app import app
from flask import render_template, request
from flask import Blueprint

transactions_blueprint = Blueprint('transactions', __name__)
@transactions_blueprint.route('/transactions')
def transactions():
    return render_template('transactions/transactions.html')

@transactions_blueprint.route('/set_budget')
def set_budget():
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