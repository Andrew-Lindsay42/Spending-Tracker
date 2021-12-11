from flask import Flask, render_template, request, redirect
from flask import Blueprint

merchants_blueprint = Blueprint('merchants', __name__)

# INDEX
# GET '/merchants'
@merchants_blueprint.route('/merchants')
def merchants():

    return render_template('merchants/index.html')

# SHOW
# GET '/merchants/new'
@merchants_blueprint.route('/merchants/new')
def new_merchant():

    return render_template('merchants/new.html')

# CREATE
# POST '/merchants'
@merchants_blueprint.route('/merchants', methods = ['POST'])
def create_merchant():

    return redirect('merchants/new.html')

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

    return redirect('merchants/show.html')

# DELETE
# DELETE '/merchants/<id>
@merchants_blueprint.route('/merchants/<int:id>/delete', methods = ['POST'])
def delete_merchant(id):
    
    return redirect('/merchants')
