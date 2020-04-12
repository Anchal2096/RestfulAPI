from extensions import db

books_list = []


def get_last_id():
    if books_list:
        last_book = books_list[-1]
    else:
        return 1
    return last_book.id + 1


class Books(db.Model):
    __tablename__ = 'Books'

    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), nullable=False)
    Amazon_URL = db.Column(db.String(200))
    Author = db.Column(db.String(100))
    Genre = db.Column(db.String(100))

    @classmethod
    def get_value_by_id(cls, book_id):
        return cls.query.filter_by(id=book_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_by_id(cls, book_id):
        cls.query.filter_by(id=book_id).delete()
        db.session.commit()
