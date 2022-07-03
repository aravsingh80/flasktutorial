from flask import render_template, flash, redirect, url_for, request
from .models import Category
from ..models import Todo
from . import task
from .forms import TaskForm
from .. import db
from datetime import datetime

@task.route('/create-task', methods=['GET', 'POST'])
def tasks():
    check= None
    date= datetime.now()
    now= date.strftime("%Y-%m-%d")

    categories = [Category(name="Business"), Category(name="Personal"), Category(name="Other")]
    for c in categories:
        db.session.add(c)
    db.session.commit()
    
    form= TaskForm()
    form.category.choices =[(category.id, category.name) for category in Category.query.all()]
    todo= Todo.query.all()
    if request.method == "POST":
        if request.form.get('taskDelete') is not None:
            deleteTask = request.form.get('checkedbox')
            if deleteTask is not None:
                todo = Todo.query.filter_by(id=int(deleteTask)).one()
                db.session.delete(todo)
                db.session.commit()
                return redirect(url_for('task.tasks'))
            else:
                check = 'Please check-box of task to be deleted'

        elif form.validate_on_submit():
            selected= form.category.data
            category= Category.query.get(selected)
            todo = Todo(title=form.title.data, date=form.date.data, time= form.time.data, category= category.name)
            db.session.add(todo)
            db.session.commit()
            flash('Congratulations, you just added a new note')
            return redirect(url_for('task.tasks'))

    return render_template('tasks.html', title='Create Tasks', form=form, todo=todo, DateNow=now, check=check)
