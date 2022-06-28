from flask import Flask
# import os
# print(os.getcwd())
from core.config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# from .task import task as task_blueprint
# app.register_blueprint(task_blueprint)

# @app.shell_context_processor
# def make_shell_context():
#     return {'Todo': Todo, 'Category':Category}

# if __name__ == "__main__":
#     app.run(debug=True)