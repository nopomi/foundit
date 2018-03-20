from flask import render_template
from app import app
from app.forms import LoginForm

# Controllers

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miska'}
    form = LoginForm()
    return render_template('pages/index.html', form=form)

@app.route('/mylist')
def list():
    form = LoginForm()
    return render_template('pages/mylist.html', form=form)

@app.route('/help')
def help():
    form = LoginForm()
    return render_template('pages/help.html', form=form)

@app.route('/login', methods=['POST'])
def login():
    #A controller for the login post command
    return redirect(url_for('/'), code=302)


# Error handlers

@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404
