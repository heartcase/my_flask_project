from flask import Blueprint, render_template
from models.database import MongoClient
web_index = Blueprint('web_index', __name__, template_folder='templates')
client = None


@web_index.route('/charts/')
@web_index.route('/tasks/')
@web_index.route('/')
def index():
    return render_template('index.html')

@web_index.route('/dataframes/', methods=['GET'])
def dataframes():
    client = MongoClient().get_client()
    DATABASE = "test"
    db = client[DATABASE]
    table_names = db.list_collection_names()
    table = []
    table_id = 1
    for each in table_names:
        size = db.command("collstats", each)['storageSize']
        table.append([table_id, each, size])
        table_id += 1
    return render_template('dataframe.html', table=table)
