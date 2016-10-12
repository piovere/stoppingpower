from flask import render_template, flash, redirect
from app import app
from stoppingpower.cmsp import *
from stoppingpower.materials import materials
from forms import StoppingPowerForm

@app.route('/')
@app.route('/index')
def index():
    heyyyyy = "SCIENCE"
    return render_template('index.html',
                           heyyyyy=heyyyyy)


@app.route('/cmsp', methods=['GET', 'POST'])
def cmsp_page():
    form = StoppingPowerForm()
    print form.errors
    if form.validate_on_submit():
        if form.per_nucleon_bool is True:
            t = float(form.incident_t.data) * float(form.incident_a.data)
        else:
            t = float(form.incident_t.data)
        poo = S_c(
            float(form.incident_z.data),
            materials[form.material.data],
            t,
            float(form.incident_a.data)
        )
    else:
        poo = None
    return render_template('cmsp.html',
                           form=form,
                           poo=poo)
