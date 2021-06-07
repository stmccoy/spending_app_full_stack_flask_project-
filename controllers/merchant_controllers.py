from app import app
from flask import render_template, request, redirect, url_for
from flask import Blueprint
from session import session
from models.extras import Merchant
from models.frequent_trades import FrequentTrade
import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository
import repositories.frequent_trade_repository as frequent_trade_repository

merchants_blueprint = Blueprint('merchants', __name__)

@merchants_blueprint.route('/merchants')
def merchants():
    user = user_repository.select(session)  
    merchants = frequent_trade_repository.select_all_by_user(str(user.id))
    return render_template('merchants/merchants.html', merchants=merchants, user=user)

@merchants_blueprint.route('/add_favourite_merchant', methods=['GET', 'POST'])
def add_merchant():
    user = user_repository.select(session) 
    if request.method == 'POST':
        user = user_repository.select(session) 
        merchant_name = request.form['merchant_name']
        merchant = Merchant(merchant_name)
        merchant.website = request.form['merchant_website']
        merchant_repository.save(merchant)
        frequent_trade = FrequentTrade(user, merchant)
        frequent_trade_repository.save(frequent_trade)
        return redirect(url_for('merchants.merchants'))    
    return render_template('merchants/add_favourite_merchant.html', user=user)

@merchants_blueprint.route("/merchant/<id>/delete", methods=['POST'])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect(url_for('merchants.merchants'))

@merchants_blueprint.route("/merchant/<id>/update", methods=['GET','POST'])
def update_merchant(id):
    user = user_repository.select(session) 
    merchant = merchant_repository.select(id)
    if request.method == 'POST':
        merchant.merchant_name = request.form['merchant_name']
        merchant.website = request.form['merchant_website']
        merchant_repository.update(merchant)
        return redirect(url_for('merchants.merchants'))
    return render_template('merchants/edit_merchant.html', merchant=merchant, user=user)
    

