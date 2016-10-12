from flask import render_template
from app import app
from stoppingpower.cmsp import S_c
from stoppingpower.range import rangeout, exit_energy
from stoppingpower.materials import materials
from stoppingpower.range import nuclear_fraction
from forms import StoppingPowerForm, RangeForm, ExitForm, NuclearInteractionFractionForm

@app.route('/')
@app.route('/index')
def index():
    heyyyyy = "SCIENCE"
    return render_template('index.html',
                           heyyyyy=heyyyyy)


@app.route('/cmsp', methods=['GET', 'POST'])
def cmsp_page():
    form = StoppingPowerForm()

    if form.validate_on_submit():
        if form.per_nucleon_bool.data is True:
            t = float(form.incident_t.data) * float(form.incident_a.data)
        else:
            t = float(form.incident_t.data)
        sc = S_c(float(form.incident_z.data), materials[form.material.data], t, float(form.incident_a.data))
    else:
        sc = None
    return render_template('cmsp.html',
                           form=form,
                           sc=sc)


@app.route('/range', methods=['GET', 'POST'])
def range_page():
    form = RangeForm()

    if form.validate_on_submit():
        if form.per_nucleon_bool.data is True:
            t = float(form.incident_t.data) * float(form.incident_a.data)
        else:
            t = float(form.incident_t.data)
        z = float(form.incident_z.data)
        a = float(form.incident_a.data)
        r = rangeout(z, materials[form.material.data], t, a)
    else:
        r = None
    return render_template(
        'range.html',
        form=form,
        r=r
    )


@app.route('/exit', methods=['GET', 'POST'])
def exit_energy_page():
    form = ExitForm()

    if form.validate_on_submit():
        if form.per_nucleon_bool.data is True:
            t = float(form.incident_t.data) * float(form.incident_a.data)
        else:
            t = float(form.incident_t.data)
        z = float(form.incident_z.data)
        a = float(form.incident_a.data)
        thickness = float(form.thickness.data)
        ee = exit_energy(z, materials[form.material.data], t, a, thickness)
        eepn = ee / a
        deposited = t - ee
    else:
        ee = None
        eepn = None
        deposited = None
    return render_template(
        'exitenergy.html',
        form=form,
        ee=ee,
        eepn=eepn,
        deposited=deposited
    )


@app.route('/nuclear', methods=['GET', 'POST'])
def nuclear_interaction_fraction_page():
    form = NuclearInteractionFractionForm()

    if form.validate_on_submit():
        inter_frac = nuclear_fraction(
            float(form.incident_a.data),
            materials[form.material.data],
            float(form.thickness.data)
        )
    else:
        inter_frac = None
    return render_template(
        'nuclear.html',
        form=form,
        inter_frac=inter_frac
    )
