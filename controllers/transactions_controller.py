from flask import Flask, render_template, request, redirect
from flask import Blueprint

transactions_blueprint = Blueprint('transactions', __name__)

# INDEX
# GET '/transactions'
@transactions_blueprint.route('/transactions')
def transactions():

    return render_template('transactions/index.html')

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

    return render_template('transactions/show.html')

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
# DELETE '/transactions/<id>
@transactions_blueprint.route('/transactions/<int:id>/delete', methods = ['POST'])
def delete_transaction(id):
    
    return redirect('/transactions')
