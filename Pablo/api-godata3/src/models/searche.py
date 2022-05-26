from sql_alchemy import banco


class SearcheModel(banco.Model):
    __tablename__ = 'searches'

    searche_id = banco.Column(banco.Integer, primary_key=True, nullable=False)
    title = banco.Column(banco.Text)
    keywords = banco.Column(banco.Text)
    abstract = banco.Column(banco.Text)
    year = banco.Column(banco.Integer)
    type_publication = banco.Column(banco.Text)
    doi = banco.Column(banco.Text)

    def __init__(self, title, keywords, abstract, year, type_publication, doi):
        self.title = title
        self.keywords = keywords
        self.abstract = abstract
        self.year = year
        self.type_publication = type_publication
        self.doi = doi

    def json(self):
        return {
            'search_id':self.searche_id,
            'title':self.title,
            'keywords': self.keywords,
            'abstract':self.abstract,
            'year': self.year,
            'type_publication': self.type_publication,
            'doi': self.doi
        }


    def save_searche(self):
        banco.session.add(self)
        banco.session.commit()
    
