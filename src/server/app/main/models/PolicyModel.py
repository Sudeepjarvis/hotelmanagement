from . import db
import datetime

class PolicyModel(db.Model):
    
    __tablename__ = 'policy'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           nullable=True, default=datetime.datetime.now())