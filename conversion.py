from flask import Flask, render_template, request, g
from forms import ConversionForm
from util import units
from flask_bootstrap import Bootstrap
from flask_sijax import Sijax
from helpers import SijaxHandler
from logging.handlers import SMTPHandler, RotatingFileHandler
import os

#LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')

app = Flask(__name__)

app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'

bootstrap = Bootstrap(app)
sijax = Sijax(app)

app.secret_key = os.urandom(16) or b'\xf1qE\x8d[\x1e\xb8\x80q\xd8F\xb8\xb4\\=\xb2\xca\xd0VU>5R\x9d'

app.config['LOG_TO_STDOUT'] = os.environ.get('LOG_TO_STDOUT')

if not app.debug and not app.testing:
   if app.config['LOG_TO_STDOUT']:
      stream_handler = logging.StreamHandler()
      stream_handler.setLevel(logging.INFO)
      app.logger.addHandler(stream_handler)
   else:
      if not os.path.exists('logs'):
         os.mkdir('logs')
         file_handler = RotatingFileHandler('logs/workon.log', maxBytes=10240, backupCount=10)
         file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s'
            '[in %(pathname)s:%(lineno)d]'
         ))
         file_handler.setLevel(logging.INFO)
         app.logger.addHandler(file_handler)
         app.logger.setLevel(logging.INFO)
         app.logger.info('units-conversion startup')

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
