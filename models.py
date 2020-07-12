from app import db
from flask_sqlalchemy import SQLAlchemy



class FundRaiser(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    ngoName  = db.Column(db.String(80))
    fundRaisingName = db.Column(db.String(80))
    amountCollected = db.Column(db.Integer)
    amountTargeted = db.Column(db.Integer)

    def __init__(self, ngoName, fundRaisingName, amountTargeted):
        self.ngoName  = ngoName
        self.fundRaisingName = fundRaisingName
        self.amountTargeted = amountTargeted