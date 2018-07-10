from flask import Blueprint, render_template

web_index = Blueprint('web_index    ', __name__, template_folder='templates')


@web_index.route('/dataframes/')
@web_index.route('/charts/')
@web_index.route('/tasks/')
@web_index.route('/')
def index():
    return render_template('index.html')
