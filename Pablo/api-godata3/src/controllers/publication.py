from flask_restful import Resource, request, reqparse
from src.models.publication import PublicationModel
from src.services.dofile import Dofile
from werkzeug.utils import secure_filename


class Publication(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('author')
    atributos.add_argument('title')
    atributos.add_argument('keywords')
    atributos.add_argument('abstract')
    atributos.add_argument('year')
    atributos.add_argument('type_publication')
    atributos.add_argument('doi')

    def get(self):
        author = request.args.get('author')
        title = request.args.get('title')
        keywords = request.args.get('keywords')
        abstract = request.args.get('abstract')
        year = request.args.get('year', type=int)
        type_publication = request.args.get('type_publication')
        doi = request.args.get('doi')

        if author:
            res = PublicationModel.query.filter_by(author = author)
        elif title:
            res = PublicationModel.query.filter_by(title = title)
        elif keywords:
            res = PublicationModel.query.filter(PublicationModel.keywords.like(f'%{keywords}%'))
        elif abstract:
            res = PublicationModel.query.filter(PublicationModel.abstract.like(f'%{abstract}%'))
        elif year:
            res = PublicationModel.query.filter_by(year = year)
        elif type_publication:
            res = PublicationModel.query.filter(PublicationModel.type_publication.like(f'%{type_publication}%'))
        elif doi:
            res = PublicationModel.query.filter(PublicationModel.doi.like(f'%{doi}%'))
        else: 
            res = PublicationModel.query.all()

        return{'publications': [publication.json() for publication in res]}


    def post(self):
        if 'file' not in request.files:
            return {"message": "File not found." }, 400
        
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save('input/' + filename)

        do_file = Dofile()
        df_bib = do_file.read_file_bib(filename)
        new_df_bib = do_file.select_col(df_bib)
        file_exp = do_file.get_file(new_df_bib, filename, 'json')

        return {'publications' : file_exp}, 200
