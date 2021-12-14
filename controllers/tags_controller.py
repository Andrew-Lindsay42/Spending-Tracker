from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag
from repositories import tag_repository as tag_repo
from repositories import user_repository as user_repo

tags_blueprint = Blueprint('tags', __name__)

# INDEX
# GET '/tags'
@tags_blueprint.route('/tags')
def tags():
    active_tags = tag_repo.get_active()
    inactive_tags = tag_repo.get_inactive()
    user = user_repo.select_all()[0]
    till_payday = user_repo.get_days_till_payday(user.id)
    return render_template('tags/index.html', active_tags = active_tags, inactive_tags = inactive_tags, title = 'All Tags', days_till_payday = till_payday)

# SHOW
# GET '/tags/new'
@tags_blueprint.route('/tags/new')
def new_tag():
    user = user_repo.select_all()[0]
    till_payday = user_repo.get_days_till_payday(user.id)
    return render_template('tags/new.html', title = 'New Tag', days_till_payday = till_payday)

# CREATE
# POST '/tags'
@tags_blueprint.route('/tags/new', methods = ['POST'])
def create_tag():
    name = request.form['name']
    icon = request.form['icon']
    new_tag = Tag(name, True, icon)
    tag_repo.save(new_tag)
    user = user_repo.select_all()[0]
    till_payday = user_repo.get_days_till_payday(user.id)
    return render_template('tags/new.html', title = 'New Tag', message = "Tag added!", days_till_payday = till_payday)

# SHOW
# GET '/tags/<id>
@tags_blueprint.route('/tags/<int:id>')
def show_tag(id):
    return redirect('/tags')

# EDIT
# GET '/tags/<id>/edit
@tags_blueprint.route('/tags/<int:id>/edit')
def edit_tag(id):
    tag = tag_repo.select(id)
    user = user_repo.select_all()[0]
    till_payday = user_repo.get_days_till_payday(user.id)
    return render_template('tags/edit.html', tag = tag, title = 'Edit Tag', days_till_payday = till_payday)

# UPDATE
# PUT '/tags/<id>
@tags_blueprint.route('/tags/<int:id>/edit', methods = ['POST'])
def update_tag(id):
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
    updated_tag = Tag(name, active, icon, id)
    tag_repo.update(updated_tag)
    return redirect('/tags')

# DELETE
# DELETE '/tags/<id>
@tags_blueprint.route('/tags/<int:id>/delete', methods = ['POST'])
def delete_tag(id):
    tag_repo.delete(id)
    return redirect('/tags')
