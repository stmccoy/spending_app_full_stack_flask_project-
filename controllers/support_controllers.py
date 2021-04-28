from app import app
from flask import render_template, request
from flask import Blueprint


support_blueprint = Blueprint('support', __name__)
@support_blueprint.route('/support')
def support():
    return render_template('support/support.html')
