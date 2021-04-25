from app import app
from flask import render_template, request, redirect, url_for
from flask import Blueprint
from session import session
from models.extras import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint('merchants', __name__)

@merchants_blueprint.route('/merchants')
def merchants():
    merchants = merchant_repository.select_all()
    return render_template('merchants/merchants.html', merchants=merchants)

@merchants_blueprint.route('/add_favourite_merchant', methods=['GET', 'POST'])
def add_merchant():
    if request.method == 'POST':
        merchant_name = request.form['merchant_name']
        if 'merchant_website' in request.form:
            merchant_website = request.form['merchant_website']
        merchant = Merchant(merchant_name)
        merchant.website = request.form['merchant_website']
        merchant_repository.save(merchant)
        return redirect(url_for('merchants.merchants'))    
    return render_template('merchants/add_favourite_merchant.html')