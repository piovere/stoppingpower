from flask.ext.wtf import Form
from wtforms import BooleanField, IntegerField, DecimalField, SelectField
from wtforms.validators import DataRequired
from stoppingpower.materials import materials


class StoppingPowerForm(Form):
    incident_z = IntegerField('incident_z', validators=[DataRequired()])
    incident_a = IntegerField('incident_a', validators=[DataRequired()])
    incident_t = DecimalField('incident_t', validators=[DataRequired()])
    per_nucleon_bool = BooleanField('per_nucleon_bool', validators=[DataRequired()])
    material = SelectField('material',
                           choices=zip(materials.keys(), materials.keys()))
