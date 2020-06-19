import json
from collections import OrderedDict

tables = [('TA','Tables'), ('LU', 'Length Units'), ('AU', 'Area Units'), ('VU', 'Volume Units'), 
        ('MU', 'Mass Units'), ('DU', 'Density Units'), ('VLFU', 'Volumetric Liquid Flow Unit'),
        ('VGFU', 'Volume Gas Flow Units'), ('MFU', 'Mass Flow Units'), ('HPU', 'High Pressure Unit'),
        ('LPU', 'Low Pressure Units'), ('SU', 'Speed Unit'), ('TU', 'Torque Units'), ('DVU', 'Dynamic Viscosity Units'),
        ('KVU', 'Kinematic Viscosity Units'), ('TCF', 'Temperature Conversion Formulas')]

units = {
    'TA': OrderedDict([
        ('unit', 'Unit'),
        ('unit', 'Unit')
    ]),
   
    'LU': OrderedDict([
        (1,'Millimeters(mm)'),
        (10,'Centimeters(cm)'),
        (1000,'Meters(m)'),
        (1000000,'Kilometers(km)'),
        (25.4,'Inches(in)'),
        (304.8,'Feet(ft)'),
        (914.4,'Yards(yd)'),
        (1609344,'Miles(mi)')
    ]),
  
    'AU': OrderedDict([
        (.01, 'Millimiter square(mm\u00b2)'),
        (1, 'Centimeter square(cm\u00b2'),
        (10000, 'Meter square(m\u00b2)'),
        (10000000000, 'Kilometer square(km\u00b2)'),
        (6.4516, 'Inch square(in\u00b2)'),
        (929.0304, 'Foot square(ft\u00b2)'),
        (8361.2736, 'Yard squre(yd\u00b2)'),
        (25899881103.36, 'Mile square(mi\u00b2)'),
        (100000000, 'Hectares'),
        (40468564, 'Acres')
    ]),

    'VU': OrderedDict([
        (1, 'Centimeter cube(cm\u00b3)'),
        (1000000, 'Meter cube(m\u00b3)'),
        (.001, 'Millilter'),
        (1000, 'Liter(l)'),
        (16.38706, 'Inch cube(in\u00b3)'),
        (28316.85, 'Foot cube(ft\u00b3)'),
        (3785.41, 'US gallons(US gal)'),
        (4545.4546, 'Imperial gallons(Imp. gal)'),
        (158982.51, 'US barrel(US brl)')
    ]),

    'MU': OrderedDict([
        (1, 'Grams(g)'),
        (1000, 'Kilograms(kg)'),
        (100000, 'Metric tonne(tonne)'),
        (907184.74, 'Short ton(shton)'),
        (1016047, 'Long ton(Lton)'),
        (453.59237, 'Pounds(lb)'),
        (28.34952, 'Ounces(oz)')
    ]),

    'DU': OrderedDict([
        (1, 'Gram per millimeter(g/ml)'),
        (0.001, 'Kilogram per meter cube(kg/m\u00b3)'),
        (0.01602, 'Pound per foot cube(lb/ft\u00b3)'),
        (2.768013, 'Pound per inch cube(lb/in\u00b3)')
    ]),

    'VLFU': OrderedDict([
        (1, 'Liter per second(L/sec)'),
        (0.0167, 'Liter per minute(L/min)'),
        (0.28, 'Meter cube per hour(M\u00b3/hr)'),
        (0.4719, 'Foot cube per min(ft\u00b3/min)'),
        (0.0078666, 'Foot cube per hour(ft\u00b3/hr)'),
        (0.0631, 'US gallons per min(gal/min)'),
        (0.00184, 'US barrels per day(US brl/day)')
    ]),

    'VGFU': OrderedDict([
        (1, 'Normal meter cube per hour(Nm\u00b3/hr'),
        (0.02832, 'Standard cubic feet per hour(scf/h)'),
        (1.698999, 'Standard cubic feet per minute(scf/m)')
    ]),

    'MFU': OrderedDict([
        (1, 'Kilogram per hour(kg/h)'),
        (0.45359991, 'Pound per hour(lb/h)'),
        (0.003597, 'Kilogram per second(kg/s)'),
        (1000, 'Ton per hour(t/h)')
    ]),

    'HPU': OrderedDict([
        (1, 'Bar(bar)'),
        (0.06895002, 'Pound per square inch(psi)'),
        (0.01, 'Kilopascal(kPa)'),
        (10, 'Megapascal(Mpa)'),
        (0.98069983, 'Kilogram force per centimeter square(kgf/cm\u00b2'),
        (0.0013333, 'Millimeter of mecury(mm Hg)'),
        (1.01299983, 'Atmospheres(atm)')
    ]),

    'LPU': OrderedDict([
        (1, 'Meter of water(mH\u2082)'),
        (0.30481337, 'Foot of water(ftH\u2082O)'),
        (0.135937183, 'Centimeter of mecury(cmHg)'),
        (0.34529874, 'Inches of mecury(inHg)'),
        (0.0254028, 'Inches of water(inH\u2082O)'),
        (0.000101978, 'Pascal(Pa)')
    ]),

    'SU': OrderedDict([
        (1, 'Meter per second(m/s)'),
        (0.017, 'Meter per minute(m/min)'),
        (0.2778, 'Kilometer per hour(km/h)'),
        (0.30479, 'Foot per second(ft/s)'),
        (0.00508, 'Foot per minute(ft/min)'),
        (0.4470, 'Miles per hour(mi/h)')
    ]),

    'TU': OrderedDict([
        (1, 'Newton meter(Nm)'),
        (9.80661358, 'Kilogram force meter(kgfm)'),
        (1.35582, 'Foot pound(ftlb)'),
        (0.112985, 'Inch pound(inlb)')
    ]),

    'DVU': OrderedDict([
        (1, 'Centipoise*(cp)'),
        (100, 'Poise(poise)'),
        (1488.095238, 'Pound per foot second(lb/(ft.s)')
    ]),

    'KVU': OrderedDict([
        (1, 'Centistoke*(cs)'),
        (100, 'Stoke(St)'),
        (90909.0909, 'Foot square per second(ft\u00b2/s)'),
        (1, 'meter square per second(m\u00b2/s)')
    ]),

    'TCF': OrderedDict([
        ('c', 'Degree Celsius(\u00b0C)'),
        ('f', 'Degree Fahrenheit(\u00b0F)'),
        ('k', 'Kelvin(K)')
    ])
}
