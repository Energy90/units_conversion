from flask import Flask, render_template, request, g
from forms import ConversionForm
from util import units
from flask_bootstrap import Bootstrap
from flask_sijax import Sijax
from helpers import SijaxHandler
import os

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'development'

app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'

bootstrap = Bootstrap(app)
sijax = Sijax(app)
#SECRET_KEY = os.environ.get('SECRET_KEY') or 'let-use-units-conversion-table'



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

   if g.sijax.is_sijax_request:
      # the request looks like a valid Sijax request
      # let's register the handlers and tell Sijax to process it
      g.sijax.register_object(SijaxHandler)
      return g.sijax.process_request()

   form = ConversionForm()
    
   return render_template('index.html', form=form)
