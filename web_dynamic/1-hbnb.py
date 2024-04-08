#!/usr/bin/python3
"""This module is used for getting the html page"""
from flask import Flask, render_template
import uuid
from models import storage
app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/1-hbnb')
def display_hbnb():
    """Generating page with menu of states/cities"""
    the_states = storage.all('State')
    the_amenities = storage.all('Amenity')
    the_places = storage.all('Place')
    the_cache_id = uuid.uuid4()
    return render_template('1-hbnb.html',
                           states=the_states,
                           amenities=the_amenities,
                           places=the_places,
                           cache_id=the_cache_id)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Closing storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)