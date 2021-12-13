from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag
from repositories import tag_repository as tag_repo

tags_blueprint = Blueprint('tags', __name__)

# INDEX
# GET '/tags'
@tags_blueprint.route('/tags')
def tags():
    active_tags = tag_repo.get_active()
    inactive_tags = tag_repo.get_inactive()
    return render_template('tags/index.html', active_tags = active_tags, inactive_tags = inactive_tags)

# SHOW
# GET '/tags/new'
@tags_blueprint.route('/tags/new')
def new_tag():

    return render_template('tags/new.html')

# CREATE
# POST '/tags'
@tags_blueprint.route('/tags', methods = ['POST'])
def create_tag():
    name = request.form['name']
    icon = request.form['icon']
    new_tag = Tag(name, True, icon)
    tag_repo.save(new_tag)
    return redirect(request.referrer)

# SHOW
# GET '/tags/<id>
@tags_blueprint.route('/tags/<int:id>')
def show_tag(id):

    return render_template('/tags')

# EDIT
# GET '/tags/<id>/edit
@tags_blueprint.route('/tags/<int:id>/edit')
def edit_tag(id):
    tag = tag_repo.select(id)
    return render_template('tags/edit.html', tag = tag)

# UPDATE
# PUT '/tags/<id>
@tags_blueprint.route('/tags/<int:id>', methods = ['POST'])
def update_tag(id):
    name = request.form['name']
    icon = request.form['icon']
    if request.form['status'] == 'True':
        if 'active' in request.form:
            active = False
    else:
        if 'active' in request.form:
            active = True
    updated_tag = tag(name, active, icon, id)
    tag_repo.update(updated_tag)
    return redirect('/tags')

# DELETE
# DELETE '/tags/<id>
@tags_blueprint.route('/tags/<int:id>/delete', methods = ['POST'])
def delete_tag(id):
    tag_repo.delete(id)
    return redirect('/tags')
