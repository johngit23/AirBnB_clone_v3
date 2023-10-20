#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

# create an instance of flask class
app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """closes the storage on teardown"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
