from flask_restful import Resource, reqparse
from src.models.searche import SearcheModel



class Searche(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('title')
    atributos.add_argument('keywords')
    atributos.add_argument('abstract')
    atributos.add_argument('year')
    atributos.add_argument('type_publication')
    atributos.add_argument('doi')

    def get(self):
        return {'searches': [searche.json() for searche in SearcheModel.query.all()]}, 200

    def post(self):
        dados = Searche.atributos.parse_args()
        searche = SearcheModel(**dados)
        searche.save_searche()

        return searche.json(), 201