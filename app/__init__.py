from flask import Flask
from flask_bootstrap import Bootstrap
from views.index import web_index

app = Flask('web_app')
Bootstrap(app)

app.register_blueprint(web_index)

app.run()



