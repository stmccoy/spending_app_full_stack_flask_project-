import repositories.user_repository as user_repository
from session import session

from flask import Flask, render_template
app = Flask(__name__)

from controllers.support_controllers import support_blueprint
from controllers.merchant_controllers import merchants_blueprint
from controllers.account_controllers import account_blueprint
from controllers.transaction_controllers import transactions_blueprint
from controllers.tag_controllers import tag_blueprint



app.register_blueprint(support_blueprint)
app.register_blueprint(merchants_blueprint)
app.register_blueprint(account_blueprint)
app.register_blueprint(transactions_blueprint)
app.register_blueprint(tag_blueprint)

@app.route('/')
def index():
    user = user_repository.select(session) 
    return render_template("homepage/index.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)