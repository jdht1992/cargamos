from flask_restful import Resource
from config import app, db
from routes import routes
from flask_restful import Api


api = Api(app)
routes(api)

@app.before_first_request
def create_tables():
    db.create_all()



if __name__ == '__main__':
    app.run(debug=True)
