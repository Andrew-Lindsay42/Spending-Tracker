from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import transaction_repository as transaction_repo

transactions_blueprint = Blueprint('transactions', __name__)

# INDEX
# GET '/transactions'
@transactions_blueprint.route('/transactions')
def transactions():
    default_transactions_list = transaction_repo.get_last_week()
    return render_template('transactions/index.html', transactions = default_transactions_list)

# SHOW
# GET '/transactions/new'
@transactions_blueprint.route('/transactions/new')
def new_transaction():

    return render_template('transactions/new.html')

# CREATE
# POST '/transactions'
@transactions_blueprint.route('/transactions', methods = ['POST'])
def create_transaction():

    return redirect('transactions/new.html')

# SHOW
# GET '/transactions/<id>
@transactions_blueprint.route('/transactions/<int:id>')
def show_transaction(id):
    transaction = transaction_repo.select(id)
    return render_template('transactions/show.html', transaction = transaction)

# EDIT
# GET '/transactions/<id>/edit
@transactions_blueprint.route('/transactions/<int:id>/edit')
def edit_transaction(id):

    return render_template('transactions/edit.html')

# UPDATE
# PUT '/transactions/<id>
@transactions_blueprint.route('/transactions/<int:id>', methods = ['POST'])
def update_transaction(id):

    return redirect('transactions/show.html')

# DELETE
# DELETE '/transactions/<id>/delete
@transactions_blueprint.route('/transactions/<int:id>/delete', methods = ['POST'])
def delete_transaction(id):
    transaction_repo.delete(id)
    return redirect('/transactions')
