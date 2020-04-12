from flask import Flask, request, jsonify
from http import HTTPStatus
from flask_migrate import Migrate
from extensions import db
from config import Config
from models.Books import Books, get_last_id

app = Flask(__name__)

books_list = []

'''@app.route("/", methods=['GET'])
def get():
    return "HEllo World"
'''


@app.route('/books', methods=['POST'])
def post():
    data = request.get_json()

    book_data = Books(id=data.get('id'),
                      Title=data['Title'],
                      Amazon_URL=data['Amazon_URL'],
                      Author=data['Author'],
                      Genre=data['Genre'])
    book_data.save()
    return {"msg": "hello registered"}, HTTPStatus.CREATED


@app.route('/books/<int:book_id>', methods=['GET'])
def get(book_id):
    db_object = Books.get_value_by_id(book_id)
    return {"msg": "object found", "id": db_object.id, "Author": db_object.Author}, HTTPStatus.OK


@app.route('/authorupdate/<int:book_id>', methods=['PATCH'])
def patch(book_id):
    data = request.get_json()
    db_object = Books.get_value_by_id(book_id)
    db_object.Author = data.get("Author")
    db_object.save()
    return {"msg": "UPDATED"}, HTTPStatus.OK


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete(book_id):
    Books.delete_by_id(book_id)
    return {"msg": "Deleted"}, HTTPStatus.OK


if __name__ == '__main__':
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    app.run(debug=True)
