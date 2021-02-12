from flask_restful import Resource
from config import app
from routes import routes
from flask_restful import Api


api = Api(app)
routes(api)


if __name__ == '__main__':
    app.run(debug=True)
