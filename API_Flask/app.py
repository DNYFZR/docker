### Flask API ###
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from numpy import append

# Define App
app = Flask(__name__)

# Run app
if __name__ == '__main__':
    app.run(debug=True)

# Set-up SQL Alchemy & DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)

# Define data model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(80), unique= True, nullable= False)
    content = db.Column(db.String(120), unique= True, nullable= False)

    def __init__(self, title, content):
        self.title = title
        self.content = content

# Sync SQL Alchemy with Postgres
db.create_all()

# Define REST endpoints

# GET single
@app.route('/items/<id>', methods=['GET'])
def get_item(id):
    item = Item.query.get(id)
    del item.__dict__['_sa_instance_state']
    return jsonify(item.__dict__)

# GET all
@app.route('/items', methods=['GET'])
def get_items():
    items = []
    for item in db.session.query(Item).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)

# CREATE 
@app.route('/items', methods=['POST'])
def create_item():
    body = request.get_json()
    db.session.add(Item(body['title'], body['content']))
    db.session.commit()
    return 'Item created'

# UPDATE
@app.route('/items/<id>', methods=['PUT'])
def update_item(id):
    body = request.get_json()
    db.session.query(Item).filter_by(id=id).update(
        dict(title=body['title'], content=body['content'])
    )
    db.session.commit()
    return 'Item updated'

# DELETE
@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
    db.session.query(Item).filter_by(id=id).delete()
    db.session.commit()
    return 'Item deleted'