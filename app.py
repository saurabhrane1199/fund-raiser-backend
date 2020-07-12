import json
from flask import Flask, jsonify, request, redirect, url_for, render_template, flash, session
from models import FundRaiser


app = Flask(__name__)
app.secret_key = "secret"
# node_address = str(uuid4()).replace('-', '')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fundraiser.db'
db = SQLAlchemy(app)



@app.route('/', methods=['GET'])
def index():
    return jsonify("Hello WOrld ")


if __name__ == '__main__':
    app.debug=True
    db.create_all()
    app.secret_key="123"
    app.run(host='127.0.0.1', port=5000)