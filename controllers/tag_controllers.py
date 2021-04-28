from app import app
from flask import render_template, request, redirect, url_for
from flask import Blueprint
from session import session
from models.extras import *
import repositories.tag_repository as tag_repository
import repositories.user_repository as user_repository

tag_blueprint = Blueprint('tag', __name__)

@tag_blueprint.route('/add_custom_tag', methods=['GET', 'POST'])
def add_custom_tag():
    user = user_repository.select(session)
    if request.method == 'POST':
        tag_name = request.form['tag_name']
        tag = Tag(tag_name)
        if 'adult_rating' in request.form:
            tag = Tag(tag_name, True)
        user = user_repository.select(session)
        tag.user = user
        tag_repository.save(tag)
        return redirect(url_for('tag.view_tags'))
    tags = tag_repository.select_all_by_user(str(user.id))
    return render_template('tags/add_custom_tag.html', tags=tags)

@tag_blueprint.route('/view_tags', methods=['GET', 'POST'])
def view_tags():
    user = user_repository.select(session)        
    tags = tag_repository.select_all_by_user(str(user.id))
    return render_template('tags/view_tags.html', tags=tags)

@tag_blueprint.route("/tag/<id>/delete", methods=['POST'])
def delete_tag(id):
    tag_repository.delete(id)
    return redirect(url_for('tag.view_tags'))

@tag_blueprint.route("/tag/<id>/update", methods=['GET', 'POST'])
def update_tag(id):
    tag = tag_repository.select(id)
    if request.method == 'POST':
        tag.tag_name = request.form['tag_name']
        if 'adult_rating' in request.form:
            tag.adult_rating = True
        tag_repository.update(tag)
        return redirect(url_for('tag.view_tags'))
    return render_template('tags/edit_tag.html', tag=tag)
