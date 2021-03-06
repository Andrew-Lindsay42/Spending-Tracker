from flask import Flask, render_template
app = Flask(__name__)

from controllers.users_controller import users_blueprint
from controllers.merchants_controller import merchants_blueprint
from controllers.tags_controller import tags_blueprint
from controllers.transactions_controller import transactions_blueprint
app.register_blueprint(users_blueprint)
app.register_blueprint(merchants_blueprint)
app.register_blueprint(tags_blueprint)
app.register_blueprint(transactions_blueprint)

@app.route('/')
def home():
    return render_template('index.html', title = 'Spending Tracker')

if __name__ == '__main__':
    app.run(debug=True)