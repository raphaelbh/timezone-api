from flask import Flask
from flask_cors import CORS

from api import api
from swagger import swagger

app = Flask(__name__)
app.register_blueprint(api.blueprint, url_prefix='/api/v1')
app.register_blueprint(swagger.blueprint)

cors = CORS(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0")