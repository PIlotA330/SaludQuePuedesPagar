from flask import render_template, url_for, flash, redirect, request
from website import app
from website import db
from website.models import PDM
from website.forms import SearchForm_es, SearchForm_en

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('landing.html')

@app.route('/en')
def en():
    return render_template('home_en.html')

@app.route('/es')
def es():
    return render_template('home_es.html')

@app.route('/en/other')
def other_en():
    return render_template('other_en.html', title='Other')

@app.route('/es/otro')
def other_es():
    return render_template('other_es.html', title='Otro')

@app.route('/es/informacion')
def about_es():
    return render_template('about_es.html', title="Informacion")

@app.route('/en/about')
def about_en():
    return render_template('about_en.html', title="About")

@app.route('/es/buscar', methods=['GET', 'POST'])
def search_es():
    form = SearchForm_es()
    if request.method == 'POST' and form.search_type.data != None and True in [form.mental.data, form.dental.data, form.primary.data]:
        return redirect(url_for('results_en', type=form.search_type.data, city=form.city_search.data, zip=form.zip_search.data, dental=form.dental.data, mental=form.mental.data, primary=form.primary.data))
    return render_template('search_es.html', title='Buscar', form=form)

@app.route('/en/search', methods=['GET', 'POST'])
def search_en():
    form = SearchForm_en()
    if request.method == 'POST' and form.search_type.data != None and True in [form.mental.data, form.dental.data, form.primary.data]:
        return redirect(url_for('results_en', type=form.search_type.data, city=form.city_search.data, zip=form.zip_search.data, dental=form.dental.data, mental=form.mental.data, primary=form.primary.data))
    return render_template('search_en.html', title='Search', form=form)

@app.route('/es/medicinas')
def medication_es():
    return render_template('medication_es.html', title='Medicinas')

@app.route('/en/medications')
def medication_en():
    return render_template('medication_en.html', title='Medications')

@app.route('/es/documentos')
def documents_es():
    return render_template('documents_es.html', title='Documentos')

@app.route('/en/documents')
def documents_en():
    return render_template('documents_en.html', title='Documents')

@app.route('/es/resultados/<type>/<city>/<zip>/<dental>/<mental>/<primary>')
def results_es(type, city, zip, dental, mental, primary):
    form_results = []
    if type == "Ningun criterio":
        if dental == "True":
            for i in PDM.query.all():
                if i.dental == "1" and i not in form_results:
                    form_results.append(i)
        if mental == "True":
            for i in PDM.query.all():
                if i.mental == "1" and i not in form_results:
                    form_results.append(i)
        if primary == "True":
            for i in PDM.query.all():
                if i.primary == "1" and i not in form_results:
                    form_results.append(i)
    elif type == "Por Ciudad en la que reside":
        if dental == "True":
            for i in PDM.query.all():
                if i.dental == "1" and i.city==city and i not in form_results:
                    form_results.append(i)
        if mental == "True":
            for i in PDM.query.all():
                if i.mental == "1" and i.city==city and i not in form_results:
                    form_results.append(i)
        if primary == "True":
            for i in PDM.query.all():
                if i.primary == "1" and i.city==city and i not in form_results:
                    form_results.append(i)
    elif type == 'Por código postal en el que reside':
        if dental == "True":
            for i in PDM.query.all():
                if i.dental == "1" and str(i.zip)==zip and i not in form_results:
                    form_results.append(i)
        if mental == "True":
            for i in PDM.query.all():
                if i.mental == "1" and str(i.zip)==zip and i not in form_results:
                    form_results.append(i)
        if primary == "True":
            for i in PDM.query.all():
                if i.primary == "1" and str(i.zip)==zip and i not in form_results:
                    form_results.append(i)
    if len(form_results) == 0:
        return render_template('no_results_es.html', title='No Resultados')
    return render_template('search_results_es.html', title='Resultados', form_results=form_results)

@app.route('/en/results/<type>/<city>/<zip>/<dental>/<mental>/<primary>')
def results_en(type, city, zip, dental, mental, primary):
    form_results = []
    if type == "None":
        if dental == "True":
            for i in PDM.query.all():
                if i.dental == "1" and i not in form_results:
                    form_results.append(i)
        if mental == "True":
            for i in PDM.query.all():
                if i.mental == "1" and i not in form_results:
                    form_results.append(i)
        if primary == "True":
            for i in PDM.query.all():
                if i.primary == "1" and i not in form_results:
                    form_results.append(i)
    elif type == "City":
        if dental == "True":
            for i in PDM.query.all():
                if i.dental == "1" and i.city==city and i not in form_results:
                    form_results.append(i)
        if mental == "True":
            for i in PDM.query.all():
                if i.mental == "1" and i.city==city and i not in form_results:
                    form_results.append(i)
        if primary == "True":
            for i in PDM.query.all():
                if i.primary == "1" and i.city==city and i not in form_results:
                    form_results.append(i)
    elif type == "Zip Code":
        if dental == "True":
            for i in PDM.query.all():
                if i.dental == "1" and str(i.zip)==zip and i not in form_results:
                    form_results.append(i)
        if mental == "True":
            for i in PDM.query.all():
                if i.mental == "1" and str(i.zip)==zip and i not in form_results:
                    form_results.append(i)
        if primary == "True":
            for i in PDM.query.all():
                if i.primary == "1" and str(i.zip)==zip and i not in form_results:
                    form_results.append(i)
    if len(form_results) == 0:
        return render_template('no_results_en.html', title='No Results')
    return render_template('search_results_en.html', title="Results", form_results = form_results)

@app.route('/en/events')
def events_en():
    return render_template('events_en.html', title="Events")

@app.route('/es/eventos')
def events_es():
    return render_template('events_es.html', title='Eventos')

@app.route('/admin')
def admin():
    return render_template('admin.html', title='Admin')
