from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, DateField, SubmitField, SelectField
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask import Flask
from core.config import Configuration
app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __repr__(self):
        return '<Category {}>'.format(self.name)

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', coerce=int , validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d' , validators=[DataRequired()])
    time = TimeField('Time', format='%H:%M' , validators=[DataRequired()])
    submit = SubmitField('Add task')