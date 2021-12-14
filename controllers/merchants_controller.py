from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from repositories import merchant_repository as merchant_repo

merchants_blueprint = Blueprint('merchants', __name__)

# INDEX
# GET '/merchants'
@merchants_blueprint.route('/merchants')
def merchants():
    active_merchants = merchant_repo.get_active()
    inactive_merchants = merchant_repo.get_inactive()
    return render_template('merchants/index.html', active_merchants = active_merchants, inactive_merchants = inactive_merchants, title = 'All Merchants')

# SHOW
# GET '/merchants/new'
@merchants_blueprint.route('/merchants/new')
def new_merchant():
    
    return render_template('merchants/new.html', title = 'New Merchant')

# CREATE
# POST '/merchants'
@merchants_blueprint.route('/merchants/new', methods = ['POST'])
def create_merchant():
    name = request.form['name']
    icon = request.form['icon']
    new_merchant = Merchant(name, True, icon)
    merchant_repo.save(new_merchant)
    return redirect(request.referrer)

# SHOW
# GET '/merchants/<id>
@merchants_blueprint.route('/merchants/<int:id>')
def show_merchant(id):
    return redirect('/merchants')

# EDIT
# GET '/merchants/<id>/edit
@merchants_blueprint.route('/merchants/<int:id>/edit')
def edit_merchant(id):
    merchant = merchant_repo.select(id)
    return render_template('merchants/edit.html', merchant = merchant, title = 'Edit Merchant')

# UPDATE
# PUT '/merchants/<id>
@merchants_blueprint.route('/merchants/<int:id>/edit', methods = ['POST'])
def update_merchant(id):
    name = request.form['name']
    icon = request.form['icon']
    if request.form['status'] == 'True':
        if 'active' in request.form:
            active = False
        else:
            active = True
    else:
        if 'active' in request.form:
            active = True
        else:
            active = False
    updated_merchant = Merchant(name, active, icon, id)
    merchant_repo.update(updated_merchant)
    return redirect('/merchants')

# DELETE
# DELETE '/merchants/<id>
@merchants_blueprint.route('/merchants/<int:id>/delete', methods = ['POST'])
def delete_merchant(id):
    merchant_repo.delete(id)
    return redirect('/merchants')
