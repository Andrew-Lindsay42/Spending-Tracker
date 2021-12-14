from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
from repositories import user_repository as user_repo 

users_blueprint = Blueprint('users', __name__)

# EDIT
# GET '/budget_info'
@users_blueprint.route('/budget_info')
def edit_user_budget():
    user = user_repo.select_all()[0]
    return render_template('users/edit.html', user = user, title = 'Budget')

# UPDATE
# PUT '/budget_info
@users_blueprint.route('/budget_info', methods = ['POST'])
def update_user_budget():
    budget = request.form['budget']
    payday = request.form['payday']
    user = user_repo.select_all()[0]
    updated_user = User(user.name, budget, payday, user.id)
    user_repo.update(updated_user)
    return render_template('users/edit.html', user = user, title = 'Budget', message = 'Budget updated!')


# As having multiple users is outwith the scope of the project,
# all other routes are not needed in this case - we only need to be able to edit the budget.