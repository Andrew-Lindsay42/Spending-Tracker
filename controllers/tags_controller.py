from flask import Flask, render_template, request, redirect
from flask import Blueprint

tags_blueprint = Blueprint('tags', __name__)

# INDEX
# GET '/tags'
@tags_blueprint.route('/tags')
def tags():

    return render_template('tags/index.html')

# SHOW
# GET '/tags/new'
@tags_blueprint.route('/tags/new')
def new_tag():

    return render_template('tags/new.html')

# CREATE
# POST '/tags'
@tags_blueprint.route('/tags', methods = ['POST'])
def create_tag():

    return redirect('tags/new.html')

# SHOW
# GET '/tags/<id>
@tags_blueprint.route('/tags/<int:id>')
def show_tag(id):

    return render_template('tags/show.html')

# EDIT
# GET '/tags/<id>/edit
@tags_blueprint.route('/tags/<int:id>/edit')
def edit_tag(id):

    return render_template('tags/edit.html')

# UPDATE
# PUT '/tags/<id>
@tags_blueprint.route('/tags/<int:id>', methods = ['POST'])
def update_tag(id):

    return redirect('tags/show.html')

# DELETE
# DELETE '/tags/<id>
@tags_blueprint.route('/tags/<int:id>/delete', methods = ['POST'])
def delete_tag(id):
    
    return redirect('/tags')
