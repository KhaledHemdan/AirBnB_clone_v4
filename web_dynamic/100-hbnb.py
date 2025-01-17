#!/usr/bin/python3
"""
The Comment I have to write
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid



# The Comment I have to write flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'



# The Comment I have to write begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    The Comment I have to write
    The Comment I have to write
    """
    storage.close()



@app.route('/100-hbnb')
def hbnb_filters(the_id=None):
    """
    The Comment I have to write
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    return render_template('100-hbnb.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users,
                           cache_id=uuid.uuid4())



if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
