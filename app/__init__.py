from flask import Flask
from flask_bootstrap import Bootstrap
from views.index import web_index
from models.database import MongoClient
import pymongo as mg
app = Flask('web_app')
app.config.from_object('config')
Bootstrap(app)
app.register_blueprint(web_index)

client = mg.MongoClient(app.config['DB_URL'])
MongoClient(client)


app.run()


