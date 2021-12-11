from flask import Flask, render_template, request, redirect
from flask import Blueprint

users_blueprint = Blueprint('users', __name__)

# EDIT
# GET '/budget_info'
@users_blueprint.route('/budget_info')
def edit_user_budget():

    return render_template('users/edit.html')

# UPDATE
# PUT '/budget_info
@users_blueprint.route('/budget_info', methods = ['POST'])
def update_user_budget():

    return redirect('users/edit.html')


# As having multiple users is outwith the scope of the project,
# all other routes are not needed in this case - we only need to be able to edit the budget.