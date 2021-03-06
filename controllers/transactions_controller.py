import datetime
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
from repositories import transaction_repository as transaction_repo
from repositories import merchant_repository as merchant_repo
from repositories import tag_repository as tag_repo
from repositories import user_repository as user_repo

transactions_blueprint = Blueprint('transactions', __name__)

# INDEX
# GET '/transactions'
@transactions_blueprint.route('/transactions')
def transactions():
    default_transactions_list = transaction_repo.get_last_week()
    user = user_repo.select_all()[0]
    till_payday = user_repo.get_days_till_payday(user.id)
    remaining_budget = user_repo.get_remaining_budget(user.id)
    today = datetime.date.today()
    last_week = today - datetime.timedelta(days=7)
    merchants = merchant_repo.select_all()
    tags = tag_repo.select_all()
    total = transaction_repo.get_total(default_transactions_list)
    total = '{:.2f}'.format(total)
    return render_template('transactions/index.html', transactions = default_transactions_list, title = 'All Transactions', days_till_payday = till_payday, remaining_budget = remaining_budget, start_date = last_week, end_date = today, merchants = merchants, tags = tags, total = total)


# GET '/transactions', but with filter applied
@transactions_blueprint.route('/transactions', methods = ['post'])
def filtered_transactions():
    user = user_repo.select_all()[0]
    till_payday = user_repo.get_days_till_payday(user.id)
    remaining_budget = user_repo.get_remaining_budget(user.id)
    merchants = merchant_repo.select_all()
    tags = tag_repo.select_all()

    start_date = request.form['start_date']
    end_date = request.form['end_date']

    # If the start date is later than the end date, swap the dates around.
    if start_date > end_date:
        temp_date = start_date
        start_date = end_date
        end_date = temp_date
    transactions = transaction_repo.get_custom_date(start_date, end_date)

    # Check the input from the form to filter out the correct info.
    if request.form['merchant_id'] == 'no merchants':
        merchant = None
        merchant_select = 'no merchants'
    elif request.form['merchant_id'] == 'all merchants':
        merchant = 'All'
        merchant_select = 'all merchants'
    else:
        merchant = merchant_repo.select(request.form['merchant_id'])
        merchant_select = int(request.form['merchant_id'])

    transactions = transaction_repo.filter_by_merchant(merchant, transactions)

    # Check the input from the form to filter out the correct info.
    if request.form['tag_id'] == 'no tags':
        tag = None
        tag_select = 'no merchants'
    elif request.form['tag_id'] == 'all tags':
        tag = 'All'
        tag_select = 'all tags'
    else:
        tag = tag_repo.select(request.form['tag_id'])
        tag_select = int(request.form['tag_id'])

    transactions = transaction_repo.filter_by_tag(tag, transactions)
    total = transaction_repo.get_total(transactions)
    total = '{:.2f}'.format(total)
    
    return render_template('transactions/index.html', transactions = transactions, title = 'Filtered Transactions', days_till_payday = till_payday, remaining_budget = remaining_budget, start_date = start_date, end_date = end_date, merchants = merchants, tags = tags, merchant_select = merchant_select, tag_select = tag_select, total = total)

# SHOW
# GET '/transactions/new'
@transactions_blueprint.route('/transactions/new')
def new_transaction():
    today = datetime.date.today()
    merchants = merchant_repo.get_active()
    tags = tag_repo.get_active()
    user = user_repo.select_all()[0]
    till_payday = user_repo.get_days_till_payday(user.id)
    remaining_budget = user_repo.get_remaining_budget(user.id)
    return render_template('transactions/new.html', today = today, merchants = merchants, tags = tags, title = 'New Transaction', days_till_payday = till_payday, remaining_budget = remaining_budget)

# CREATE
# POST '/transactions'
@transactions_blueprint.route('/transactions/new', methods = ['POST'])
def create_transaction():
    date = request.form['date']
    amount = request.form['amount']
    description = request.form['description']

    # Check the input from the form to give the correct info for creation.
    if request.form['merchant_id'] != 'no merchant':
        merchant = merchant_repo.select(request.form['merchant_id'])
    else:
        merchant = None
    if request.form['tag_id'] != 'no tag':
        tag = tag_repo.select(request.form['tag_id'])
    else:
        tag = None
    new_transaction = Transaction(amount, date, description, merchant, tag)
    transaction_repo.save(new_transaction)

    today = datetime.date.today()
    merchants = merchant_repo.get_active()
    tags = tag_repo.get_active()
    user = user_repo.select_all()[0]
    till_payday = user_repo.get_days_till_payday(user.id)
    remaining_budget = user_repo.get_remaining_budget(user.id)
    return render_template('transactions/new.html', today = today, merchants = merchants, tags = tags, title = 'New Transaction', message = 'Transaction added!', days_till_payday = till_payday, remaining_budget = remaining_budget)

# SHOW
# GET '/transactions/<id>
@transactions_blueprint.route('/transactions/<int:id>')
def show_transaction(id):
    transaction = transaction_repo.select_for_display(id)
    user = user_repo.select_all()[0]
    till_payday = user_repo.get_days_till_payday(user.id)
    remaining_budget = user_repo.get_remaining_budget(user.id)
    return render_template('transactions/show.html', transaction = transaction, title = 'Detailed View', days_till_payday = till_payday, remaining_budget = remaining_budget)

# EDIT
# GET '/transactions/<id>/edit
@transactions_blueprint.route('/transactions/<int:id>/edit')
def edit_transaction(id):
    transaction = transaction_repo.select(id)
    merchants = merchant_repo.get_active()
    tags = tag_repo.get_active()
    user = user_repo.select_all()[0]
    till_payday = user_repo.get_days_till_payday(user.id)
    remaining_budget = user_repo.get_remaining_budget(user.id)
    return render_template('transactions/edit.html', transaction = transaction, merchants = merchants, tags = tags, title = 'Edit Transaction', days_till_payday = till_payday, remaining_budget = remaining_budget)

# UPDATE
# PUT '/transactions/<id>
@transactions_blueprint.route('/transactions/<int:id>/edit', methods = ['POST'])
def update_transaction(id):
    date = request.form['date']
    amount = request.form['amount']
    description = request.form['description']

    # Check the input from the form to give the correct info for creation.
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
