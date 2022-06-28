from core import app, db
from core.models import Todo
from core.task.models import Category

@app.shell_context_processor
def make_shell_context():
    return {'Todo': Todo, 'db': db, 'Category':Category}