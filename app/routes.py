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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request sent for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return redirect('/index')


# Error handlers

@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404
