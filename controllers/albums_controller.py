from flask import Flask, render_template, redirect
from flask import Blueprint
import repositories.album_repository as album_repository

albums_blueprint = Blueprint("albums", __name__)



# INDEX
@albums_blueprint.route('/albums')
def albums():                       # check spelling all_albums!!
    albums = album_repository.select_all()
    return render_template("albums/index.html", albums = albums) # it was wrong spelling
# show single albums detail


# CREATE



# READ
# SHOW GET '/albums/edit'

@albums_blueprint.route("/albums/<id>", methods=['GET'])
def show_album(id):
    album = album_repository.select(id)
    return render_template('albums/show.html', album = album)

# UPDATE

# # DELETE Done I'm waiting to fill in the gaps with step 2,
#  to get the details of a single album first

# @albums_blueprint.route("/albums/<id>/delete", methods=['POST'])
# def delete_album(id):
#     album_repository.delete(id)
#     pass # return redirect('/albums')

