from util import tables, units
import re

class SijaxHandler(object):
    """
    A container class for all Sijax handlers.

    Grouping all Sijax handler functions in a class
    (or a Python module) allows them all to be registered with
    a single line of code.
    """

    def categories(obj_response, table): 
        options = ''       
        for key, val in units[table].items():
            options += "<option value='%s'>%s</option>"%(key, val)

        obj_response.html('#units', options)
        obj_response.html('#units_2', options)
        

    def calculate(obj_response, value, unit_1, unit_2):
        regex = re.compile('^[-+]?[0-9]*\.?[0-9]+$')
        value = regex.match(value)
        value = value.group()

        if value:
            if (unit_1 == unit_2 == 'c') or (unit_1 == unit_2 == 'f') or (unit_1 == unit_2 == 'k'):
                val = value

            elif unit_1 == 'c' and unit_2 == 'f':
                val = (float(value)*9/5) + 32

            elif unit_1 == 'c' and unit_2 == 'k':
                val = (float(value) + 273.15) 

            elif unit_1 == 'f' and unit_2 == 'c':
                val = (float(value) - 32) * 5/9
            
            elif unit_1 == 'f' and unit_2 == 'k':
                val = (float(value) + 459.67) / 1.8

            elif unit_1 == 'k' and unit_2 == 'c':
                val = (float(value - 273.15))

            elif unit_1 == 'k' and unit_2 == 'f':
                val = (float(value) * 1.8) - 459.67
            else:
                val =  (float(value) * float(unit_1)/float(unit_2))


            obj_response.attr('#output_field', 'value', val) 

     

        

    