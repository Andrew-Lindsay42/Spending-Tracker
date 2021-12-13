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
    return render_template('users/edit.html', user = user)

# UPDATE
# PUT '/budget_info
@users_blueprint.route('/budget_info', methods = ['POST'])
def update_user_budget():

    return redirect(request.referrer)


# As having multiple users is outwith the scope of the project,
# all other routes are not needed in this case - we only need to be able to edit the budget.