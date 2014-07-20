from flask import render_template
from flask_security.utils import encrypt_password

from flask.ext.security import Security, SQLAlchemyUserDatastore, login_required

from service import app, db
from service.models import User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.before_first_request
def create_user():
    db.create_all()
    if not user_datastore.find_user(email='landowner@mail.com'):
        user_datastore.create_user(email='landowner@mail.com', password=encrypt_password('password'))
        db.session.commit()

@app.route('/')
@login_required
def index():
     return render_template('index.html')

@app.route('/property/<title_number>')
@login_required
def property(title_number):
    return "hello"


@app.after_request
def after_request(response):
    response.headers.add('Content-Security-Policy', "default-src 'self' 'unsafe-inline' data:") # can we get some guidance on this?
    response.headers.add('X-Frame-Options', 'deny')
    response.headers.add('X-Content-Type-Options', 'nosniff')
    response.headers.add('X-XSS-Protection', '1; mode=block')
    return response
