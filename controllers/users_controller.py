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
    till_payday = user_repo.get_days_till_payday(user.id)
    remaining_budget = user_repo.get_remaining_budget(user.id)
    return render_template('users/edit.html', user = user, title = 'Budget', days_till_payday = till_payday, remaining_budget = remaining_budget)

# UPDATE
# PUT '/budget_info
@users_blueprint.route('/budget_info', methods = ['POST'])
def update_user_budget():
    budget = request.form['budget']
    payday = request.form['payday']
    user = user_repo.select_all()[0]
    updated_user = User(user.name, budget, payday, user.id)
    user_repo.update(updated_user)
    till_payday = user_repo.get_days_till_payday(user.id)
    remaining_budget = user_repo.get_remaining_budget(user.id)
    return render_template('users/edit.html', user = updated_user, title = 'Budget', message = 'Budget updated!', days_till_payday = till_payday, remaining_budget = remaining_budget)


# As having multiple users is outwith the scope of the project,
# all other routes are not needed in this case - we only need to be able to edit the budget.