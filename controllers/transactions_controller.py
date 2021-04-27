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
import repositories.frequent_trade_repository as frequent_trade_repository


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
        tag_name = request.form['tag']
        tag = tag_repository.select_by_name(tag_name)[0]
        transaction.tag = tag
        transaction_repository.save(transaction)
        return redirect(url_for('transactions.transactions'))
    user = user_repository.select(session)  
    merchants = frequent_trade_repository.select_all_by_user(str(user.id))
    tags = tag_repository.select_all_by_user(str(user.id))
    transaction_priority_list = ["none", "low", "medium", "high"]
    return render_template('transactions/add_transaction.html', 
    transaction_priority_list=transaction_priority_list, merchants=merchants, tags=tags)


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
        tag_name = request.form['tag']
        tag = tag_repository.select_by_name(tag_name)[0]
        direct_debit.tag = tag
        direct_debit.merchant = merchant
        direct_debit.reoccurence_frequency_amount = request.form['reoccurence_frequency_amount']
        direct_debit_repository.save(direct_debit)
        #need to fix table to allow for string and add freq amount type 
        return redirect(url_for('transactions.transactions'))
    user = user_repository.select(session)  
    merchants = frequent_trade_repository.select_all_by_user(str(user.id))
    tags = tag_repository.select_all_by_user(str(user.id))
    direct_debit_priority_list = ["none", "low", "medium", "high"]
    direct_debit_time_scales = ["week", "fortnight", "month", "year"]
    return render_template('direct_debit/add_direct_debit.html', direct_debit_priority_list=direct_debit_priority_list, direct_debit_time_scales=direct_debit_time_scales, merchants=merchants, tags=tags)

@transactions_blueprint.route('/add_debt', methods=['GET', 'POST'])
def add_debt():
    if request.method == "POST":
        user = user_repository.select(session)
        value = request.form['value']
        description = request.form['description']
        debt = Debt(user, value, description)
        debt.date = request.form['date']
        # if 'priority_rating' in request.form:
        debt.priority_rating = request.form['priority_rating']
        # if 'merchant' in request.form:
        merchant_name = request.form['merchant']
        #if statement for if merchant = [] do add merchant method else do below
        merchant = merchant_repository.select_by_name(merchant_name)[0]
        debt.merchant = merchant
        # if 'tag' in request.form:
        tag_name = request.form['tag']
        tag = tag_repository.select_by_name(tag_name)[0]
        debt.tag = tag
        debt.reoccurence_frequency_amount = request.form['reoccurence_frequency_amount']
        debt.interest = request.form['interest']
        debt.late_payment_fine = request.form['late_payment_fine']
        debt.pay_off_date = request.form['pay_off_date']
        debt_repository.save(debt)
        #need to fix table to allow for string and add freq amount type 
        return redirect(url_for('transactions.transactions'))
    user = user_repository.select(session)  
    merchants = frequent_trade_repository.select_all_by_user(str(user.id))
    tags = tag_repository.select_all_by_user(str(user.id))
    debt_priority_list = ["none", "low", "medium", "high"]
    debt_time_scales = ["week", "fortnight", "month", "year"]
    return render_template('debt/add_debt.html', debt_priority_list=debt_priority_list, debt_time_scales=debt_time_scales, merchants=merchants, tags=tags)

@transactions_blueprint.route('/transaction_delete/<transaction_type>/<id>/delete', methods=['POST'])
def delete_transaction(id, transaction_type):
    if transaction_type == 'transaction':
        transaction_repository.delete(id)
    elif transaction_type == 'direct_debit':
        direct_debit_repository.delete(id)
    elif transaction_type == 'debt':
        debt_repository.delete(id)
    return redirect(url_for('transactions.transactions'))

@transactions_blueprint.route('/transaction_edit/<transaction_type>/<id>/edit', methods=['GET'])
def edit_transaction(id, transaction_type):
    user = user_repository.select(session)  
    merchants = frequent_trade_repository.select_all_by_user(str(user.id))
    tags = tag_repository.select_all_by_user(str(user.id))
    transaction_priority_list = ["none", "low", "medium", "high"]
    direct_debit_time_scales = ["week", "fortnight", "month", "year"]
    if transaction_type == 'transaction':
        transaction = transaction_repository.select(id)
        return render_template('transactions/edit_transaction.html', transaction_priority_list=transaction_priority_list, merchants=merchants, tags=tags, transaction=transaction)
    elif transaction_type == 'direct_debit':
        direct_debit = direct_debit_repository.select(id)
        return render_template('direct_debit/edit_direct_debit.html', transaction_priority_list=transaction_priority_list, merchants=merchants, tags=tags, direct_debit=direct_debit, direct_debit_time_scales=direct_debit_time_scales)
    elif transaction_type == 'debt':
        debt = debt_repository.select(id)
        return render_template('debt/edit_debt.html', transaction_priority_list=transaction_priority_list, merchants=merchants, tags=tags, debt=debt, direct_debit_time_scales=direct_debit_time_scales)        

@transactions_blueprint.route('/transaction_edit/<transaction_type>/<id>/edit', methods=['POST'])
def edit_transaction_post(id, transaction_type):
    user = user_repository.select(session)  
    if transaction_type == 'transaction':
            value = request.form['value']
            description = request.form['description']
            date = request.form['date']
            transaction = Transaction(user, value, description)
            transaction.date = date
            # if 'merchant' in request.form:
            merchant_name = request.form['merchant']
            merchant = merchant_repository.select_by_name(merchant_name)[0]
            transaction.merchant = merchant
            # if 'priority_rating' in request.form:
            priority_rating = request.form['priority_rating']
            transaction.priority_rating = priority_rating
            # if 'tag' in request.form:
            tag_name = request.form['tag']
            tag = tag_repository.select_by_name(tag_name)[0]
            transaction.tag = tag
            transaction.id = id
            transaction_repository.update(transaction)
            return redirect(url_for('transactions.transactions'))
    elif transaction_type == 'direct_debit':
            value = request.form['value']
            description = request.form['description']
            date = request.form['date']
            direct_debit = DirectDebit(user, value, description)
            direct_debit.date = date
            # if 'merchant' in request.form:
            merchant_name = request.form['merchant']
            merchant = merchant_repository.select_by_name(merchant_name)[0]
            direct_debit.merchant = merchant
            # if 'priority_rating' in request.form:
            priority_rating = request.form['priority_rating']
            direct_debit.priority_rating = priority_rating
            # if 'tag' in request.form:
            tag_name = request.form['tag']
            tag = tag_repository.select_by_name(tag_name)[0]
            direct_debit.tag = tag
            direct_debit.reoccurence_frequency_amount = request.form['reoccurence_frequency_amount']
            # if 'reoccurence_frequency_type' in request.form:
            direct_debit.reoccurence_frequency_type = request.form['reoccurence_frequency_type']
            direct_debit.id = id
            direct_debit_repository.update(direct_debit)
            return redirect(url_for('transactions.transactions'))
    elif transaction_type == 'debt':
            value = request.form['value']
            description = request.form['description']
            date = request.form['date']
            debt = Debt(user, value, description)
            debt.date = date
            # if 'merchant' in request.form:
            merchant_name = request.form['merchant']
            merchant = merchant_repository.select_by_name(merchant_name)[0]
            debt.merchant = merchant
            # if 'priority_rating' in request.form:
            priority_rating = request.form['priority_rating']
            debt.priority_rating = priority_rating
            # if 'tag' in request.form:
            tag_name = request.form['tag']
            tag = tag_repository.select_by_name(tag_name)[0]
            debt.tag = tag
            debt.reoccurence_frequency_amount = request.form['reoccurence_frequency_amount']
            # if 'reoccurence_frequency_type' in request.form:
            debt.reoccurence_frequency_type = request.form['reoccurence_frequency_type']
            debt.interest = request.form['interest']
            debt.late_payment_fine = request.form['late_payment_fine']
            debt.pay_off_date = request.form['pay_off_date']
            debt.id = id
            debt_repository.update(debt)
            return redirect(url_for('transactions.transactions'))

# @transactions_blueprint.route('/add_custom_tag', methods=['GET', 'POST'])
# def add_custom_tag():
#     user = user_repository.select(session)
#     if request.method == 'POST':
#         tag_name = request.form['tag_name']
#         tag = Tag(tag_name)
#         if 'adult_rating' in request.form:
#             tag = Tag(tag_name, True)
#         user = user_repository.select(session)
#         tag.user = user
#         tag_repository.save(tag)
#         return redirect(url_for('tags.view_tags'))
#     tags = tag_repository.select_all_by_user(str(user.id))
#     return render_template('tags/add_custom_tag.html', tags=tags)

# @transactions_blueprint.route('/view_tags', methods=['GET', 'POST'])
# def view_tags():
#     user = user_repository.select(session)        
#     tags = tag_repository.select_all_by_user(str(user.id))
#     return render_template('tags/view_tags.html', tags=tags)

# @transactions_blueprint.route("/tag/<id>/delete", methods=['POST'])
# def delete_tag(id):
#     tag_repository.delete(id)
#     return redirect(url_for('tags.view_tags'))

# @transactions_blueprint.route("/tag/<id>/update", methods=['GET', 'POST'])
# def update_tag(id):
#     tag = tag_repository.select(id)
#     if request.method == 'POST':
#         tag.tag_name = request.form['tag_name']
#         if 'adult_rating' in request.form:
#             tag.adult_rating = True
#         tag_repository.update(tag)
#         return redirect(url_for('tags.view_tags'))
#     return render_template('tags/edit_tag.html', tag=tag)
