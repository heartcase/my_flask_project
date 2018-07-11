from flask import Flask
from flask_bootstrap import Bootstrap
from views.index import web_index, data_files
from models.database import MongoClient
from flask_uploads import configure_uploads
import pymongo as mg
app = Flask('web_app')
app.config.from_object('config')

configure_uploads(app, data_files)

Bootstrap(app)
app.register_blueprint(web_index)

client = mg.MongoClient(app.config['DB_URL'])
MongoClient(client)


app.run()


