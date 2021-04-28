from app import app
from flask import render_template, request, redirect, url_for 
from flask import Blueprint
from session import session
import repositories.user_repository as user_repository

account_blueprint = Blueprint('account', __name__)

@account_blueprint.route('/account_details')
def account(): 
    user = user_repository.select(session)
    return render_template('account/account.html', user=user)

@account_blueprint.route('/edit_account_details/<id>', methods=['GET', 'POST'])
def edit_account(id): 
    user = user_repository.select(id)
    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.surname = request.form['surname']
        user.age = request.form['age']
        user.budget = request.form['budget']
        if 'dark_mode' in request.form:
            user.dark_mode = True
        else:
            user.dark_mode = False
        user_repository.update(user)
        return redirect(url_for('account.account'))
    return render_template('account/edit_account_details.html', user=user)