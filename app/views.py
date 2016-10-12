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
    if form.validate_on_submit():
        flash('Your mass stopping power is {0}'.format(form.material))
        poo = 'Your mass stopping power is {0}'.format(form.material)
    return render_template('cmsp.html',
                           form=form,
                           poo=poo)
