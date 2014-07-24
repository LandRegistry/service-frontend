from flask import render_template
from flask_security.utils import encrypt_password

from flask.ext.security import Security, SQLAlchemyUserDatastore, login_required

from service import app, db
from service.models import User, Role

import requests
import json

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
    title_url = "%s/%s/%s" % (app.config['SEARCH_API'], 'auth/titles', title_number)
    app.logger.info("Requesting title url : %s" % title_url)

    try:

      response = requests.get(title_url)
      app.logger.info("Status code %s" % response.status_code)

      if response.status_code == 400:
              return render_template('404.html'), 404
      else:
          title_json = response.json()

          property_ = title_json.get('property', '')
          address = property_.get('address','')
          payment = title_json.get('payment','')

          app.logger.info("Found the following title: %s" % title_json)
          return render_template('view_property.html',
                  proprietors = title_json.get('proprietors',''),
                  title_number = title_json.get('title_number',''),
                  tenure = property_.get('tenure',''),
                  class_of_title = property_.get('class_of_title',''),
                  house_number = address.get('house_number',''),
                  road = address.get('road',''),
                  town = address.get('town',''),
                  postcode = address.get('postcode',''),
                  price_paid = payment.get('price_paid',''))

    except requests.exceptions.RequestException as e:
      print "Request to call the search_api has failed with: %s" % e


@app.after_request
def after_request(response):
    response.headers.add('Content-Security-Policy', "default-src 'self' 'unsafe-inline' data:") # can we get some guidance on this?
    response.headers.add('X-Frame-Options', 'deny')
    response.headers.add('X-Content-Type-Options', 'nosniff')
    response.headers.add('X-XSS-Protection', '1; mode=block')
    return response
