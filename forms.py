from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired
from util import tables, units

class ConversionForm(FlaskForm):
    units_tables = SelectField("", choices=tables, validators=[DataRequired()])
    units = SelectField("", choices=[('Unit', 'Unit')], validators=[DataRequired()])
    units_2 = SelectField("", choices=[('Unit', 'Unit')], validators=[DataRequired()])
    input_field = FloatField("", validators=[DataRequired()], render_kw={"placeholder":"0.00"})
    output_field = FloatField("", render_kw={"placeholder":"0.00"})
    #convert = SubmitField("Convert")
