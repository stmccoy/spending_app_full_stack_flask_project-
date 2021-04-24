from app import app
from flask import render_template, request
from flask import Blueprint

account_blueprint = Blueprint('account', __name__)

@account_blueprint.route('/account_details')
def account():
    return render_template('account/account.html')