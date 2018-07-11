from flask import Blueprint, render_template, request
from models.database import MongoClient
from flask_uploads import UploadSet
import pandas as pd
import json
import os
import time

web_index = Blueprint('web_index', __name__, template_folder='templates')
data_files = UploadSet('csv', ('csv',))


@web_index.route('/charts/')
@web_index.route('/tasks/')
@web_index.route('/')
def index():
    return render_template('index.html')


@web_index.route('/dataframes/',  methods=['GET', 'POST'])
def dataframes():

    client = MongoClient().get_client()
    DATABASE = "test"
    db = client[DATABASE]
    if request.method == 'POST' and 'data_file' in request.files:
        filename = data_files.save(request.files['data_file'])
        collection_name = filename.replace('.csv', '')
        df = pd.read_csv(data_files.path(filename))
        df.columns = [each.replace('.', '_') for each in df.columns]
        data_dict = json.loads(df.to_json(orient='records'))
        db[collection_name].drop()
        if len(data_dict) > 0:
            db[collection_name].insert_many(data_dict)
        os.remove(data_files.path(filename))
    table_names = db.list_collection_names()
    table = []
    table_id = 1
    for each in table_names:
        size = db.command("collstats", each)['size']

        table.append([table_id, each, size])
        table_id += 1
    return render_template('dataframe.html', table=table)
