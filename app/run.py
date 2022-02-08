from flask import Flask
from api import api_blueprint
from swagger import swagger_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix='/api/v1')
app.register_blueprint(swagger_blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0")