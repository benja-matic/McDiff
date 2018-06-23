from flask import render_template, redirect, url_for
from app import app
from app.forms import FaddForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FaddForm()
    if form.validate_on_submit():
        return(redirect('/results'+"/"+str(form.value1.data)+"/"+str(form.value2.data)+"/"+str(form.value3.data)+"/"+str(form.width.data)))
    return(render_template('index.html', title='Home', form=form))

@app.route('/results/<int:val1>/<int:val2>/<int:val3>/<int:width>/')
def results(val1, val2, val3, width):
    expectation, lower, upper, ps, filename = wrapper(val1, val2, val3, width)
    expectation = round(expectation, 1)
    return(render_template('results.html', title='Results', value1=val1, value2=val2, value3=val3, width=width, expectation=expectation, filename="/static/img/{}".format(filename)))

@app.route('/acknowledgements/')
def acknowledgements():
    return(render_template('acknowledgements.html', title='Acknowledgements'))