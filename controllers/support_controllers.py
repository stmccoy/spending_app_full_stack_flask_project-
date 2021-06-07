from app import app
from flask import render_template
from flask import Blueprint
import repositories.user_repository as user_repository
from session import session


support_blueprint = Blueprint('support', __name__)
@support_blueprint.route('/support')
def support():
    user = user_repository.select(session) 
    return render_template('support/support.html', user=user)
