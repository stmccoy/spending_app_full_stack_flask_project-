from app import app
from flask import render_template, request
from flask import Blueprint

merchants_blueprint = Blueprint('merchants', __name__)

@merchants_blueprint.route('/merchants')
def merchants():
    return render_template('merchants/merchants.html')

@merchants_blueprint.route('/add_favourite_merchant')
def add_merchant():
    return render_template('merchants/add_favourite_merchant.html')