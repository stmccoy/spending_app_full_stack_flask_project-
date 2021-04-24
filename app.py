from flask import Flask, render_template
app = Flask(__name__)

from controllers.support_controller import support_blueprint
from controllers.merchant_controller import merchants_blueprint
from controllers.account_controller import account_blueprint
from controllers.transactions_controller import transactions_blueprint


app.register_blueprint(support_blueprint)
app.register_blueprint(merchants_blueprint)
app.register_blueprint(account_blueprint)
app.register_blueprint(transactions_blueprint)

@app.route('/')
def index():
    return render_template("homepage/index.html")

if __name__ == "__main__":
    app.run(debug=True)