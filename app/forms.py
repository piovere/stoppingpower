from flask_wtf import Form
from wtforms import BooleanField, IntegerField, DecimalField, SelectField
from wtforms.validators import DataRequired
from stoppingpower.materials import materials


class StoppingPowerForm(Form):
    incident_z = IntegerField('incident_z', validators=[DataRequired()])
    incident_a = IntegerField('incident_a', validators=[DataRequired()])
    incident_t = DecimalField('incident_t', validators=[DataRequired()])
    per_nucleon_bool = BooleanField('per_nucleon_bool')
    material = SelectField('material',
                           choices=zip(materials.keys(), materials.keys()))


class RangeForm(Form):
    incident_z = IntegerField('incident_z', validators=[DataRequired()])
    incident_a = IntegerField('incident_a', validators=[DataRequired()])
    incident_t = DecimalField('incident_t', validators=[DataRequired()])
    per_nucleon_bool = BooleanField('per_nucleon_bool')
    material = SelectField('material',
                           choices=zip(materials.keys(), materials.keys()))


class ExitForm(Form):
    incident_z = IntegerField('incident_z', validators=[DataRequired()])
    incident_a = IntegerField('incident_a', validators=[DataRequired()])
    incident_t = DecimalField('incident_t', validators=[DataRequired()])
    per_nucleon_bool = BooleanField('per_nucleon_bool')
    material = SelectField('material',
                           choices=zip(materials.keys(), materials.keys()))
    thickness = DecimalField('thickness', validators=[DataRequired()])


class NuclearInteractionFractionForm(Form):
    incident_a = IntegerField('incident_a', validators=[DataRequired()])
    material = SelectField('material',
                           choices=zip(materials.keys(), materials.keys()))
    thickness = DecimalField('thickness', validators=[DataRequired()])
