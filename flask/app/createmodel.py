from app import *
from flask_marshmallow import Marshmallow
from sqlalchemy import Column, Integer, String


class web(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    url_name = Column(String(100), nullable=True)
    web_name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)

    def __init__(self, url_name, web_name, description):
        self.url_name = url_name
        self.web_name = web_name
        self.description = description

class webStatus(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    url_name = Column(String(100), nullable=True)
    time_check = Column(String(250), nullable=False)
    status = Column(String(250), nullable=False)
    web_name = Column(String(250), nullable=False)

    def __init__(self, url_name, time_check, status, web_name):
        self.url_name = url_name
        self.time_check = time_check
        self.status = status
        self.web_name = web_name

ma = Marshmallow(app)
db.create_all()
class webSchema(ma.Schema):
    class Meta:
        fields = ('id', 'url_name', 'web_name', 'description')

class webstatusSchema(ma.Schema):
    class Meta:
        fields = ('id', 'url_name', 'time_check', 'status', 'web_name')

web_schema = webSchema(many=True)
webs_schema = webSchema()
webstatus_schema = webstatusSchema(many=True)
webstatus1_schema = webstatusSchema()
