from flask import Flask
from add_eqipment.views import add_equipment
from add_eqipment.database import db_session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(add_equipment, url_prefix='/add_equipment')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(debug=True)
