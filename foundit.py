from app import app, db
from app.models import User, School, Degree

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'School': School, 'Degree': Degree}
