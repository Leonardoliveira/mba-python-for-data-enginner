from sql_alchemy import banco


class PublicationModel(banco.Model):
    __tablename__ = 'publications'

    id = banco.Column(banco.Integer, primary_key=True, nullable=False)
    author = banco.Column(banco.Text)
    title = banco.Column(banco.Text)
    keywords = banco.Column(banco.Text)
    abstract = banco.Column(banco.Text)
    year = banco.Column(banco.Integer)
    type_publication = banco.Column(banco.Text)
    doi = banco.Column(banco.Text)

    def __init__(self, author, title, keywords, abstract, year, type_publication, doi):
        self.author = author
        self.title = title
        self.keywords = keywords
        self.abstract = abstract
        self.year = year
        self.type_publication = type_publication
        self.doi = doi

    def json(self):
        return {
            'author':self.author,
            'title':self.title,
            'keywords': self.keywords,
            'abstract':self.abstract,
            'year': self.year,
            'type_publication': self.type_publication,
            'doi': self.doi
        }

    
