from flask import Flask
from flask_restful import Api
from src.controllers.searche import Searche
from src.controllers.publication import Publication

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:virtual@localhost:5432/godata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_db():
    banco.create_all()


api.add_resource(Searche, '/searches')
api.add_resource(Publication, '/publications')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
