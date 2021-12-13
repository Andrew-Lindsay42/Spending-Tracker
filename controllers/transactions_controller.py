from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
from repositories import transaction_repository as transaction_repo
from repositories import merchant_repository as merchant_repo
from repositories import tag_repository as tag_repo

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
    transaction = transaction_repo.select(id)
    merchants = merchant_repo.get_active()
    tags = tag_repo.get_active()
    return render_template('transactions/edit.html', transaction = transaction, merchants = merchants, tags = tags)

# UPDATE
# PUT '/transactions/<id>
@transactions_blueprint.route('/transactions/<int:id>/edit', methods = ['POST'])
def update_transaction(id):
    date = request.form['date']
    amount = request.form['amount']
    description = request.form['description']
    if request.form['merchant_id'] != 'no merchant':
        merchant = merchant_repo.select(request.form['merchant_id'])
    else:
        merchant = None
    if request.form['tag_id'] != 'no tag':
        tag = tag_repo.select(request.form['tag_id'])
    else:
        tag = None

    updated_transaction = Transaction(amount, date, description, merchant, tag, id)
    transaction_repo.update(updated_transaction)
    return redirect('/transactions')

# DELETE
# DELETE '/transactions/<id>/delete
@transactions_blueprint.route('/transactions/<int:id>/delete', methods = ['POST'])
def delete_transaction(id):
    transaction_repo.delete(id)
    return redirect('/transactions')
