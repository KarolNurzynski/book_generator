from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    title = db.Column(db.String)
    references = db.Column(db.String)
    
    def __repr__(self):
        return "(%r, %r)" %(self.author,self.title)
