from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import merchant_repository as merchant_repo

merchants_blueprint = Blueprint('merchants', __name__)

# INDEX
# GET '/merchants'
@merchants_blueprint.route('/merchants')
def merchants():
    active_merchants = merchant_repo.get_active()
    inactive_merchants = merchant_repo.get_inactive()
    return render_template('merchants/index.html', active_merchants = active_merchants, inactive_merchants = inactive_merchants)

# SHOW
# GET '/merchants/new'
@merchants_blueprint.route('/merchants/new')
def new_merchant():

    return render_template('merchants/new.html')

# CREATE
# POST '/merchants'
@merchants_blueprint.route('/merchants/new', methods = ['POST'])
def create_merchant():

    return redirect(request.referrer)

# SHOW
# GET '/merchants/<id>
@merchants_blueprint.route('/merchants/<int:id>')
def show_merchant(id):

    return render_template('merchants/show.html')

# EDIT
# GET '/merchants/<id>/edit
@merchants_blueprint.route('/merchants/<int:id>/edit')
def edit_merchant(id):

    return render_template('merchants/edit.html')

# UPDATE
# PUT '/merchants/<id>
@merchants_blueprint.route('/merchants/<int:id>', methods = ['POST'])
def update_merchant(id):

    return redirect('merchants')

# DELETE
# DELETE '/merchants/<id>
@merchants_blueprint.route('/merchants/<int:id>/delete', methods = ['POST'])
def delete_merchant(id):
    
    return redirect('merchants')
