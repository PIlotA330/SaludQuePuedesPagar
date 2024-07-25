from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, validators, SelectField, RadioField, StringField
from website.vars import cities

class SearchForm_es(FlaskForm):
    #first start by search type
    search_type = RadioField('Tipo de búsqueda', validators=[validators.DataRequired()], choices=['Ningun criterio', 'Por Ciudad en la que reside', 'Por código postal en el que reside'])

    #second the both search types
    city_search = SelectField('Ciudad en la que reside', choices=cities)
    zip_search = StringField('Código postal en el que reside', default='00000')

    #third the boolean fields for selcting the serivce type
    dental = BooleanField('Servicio Dental')
    mental = BooleanField('Servicio de Salud Mental')
    primary = BooleanField('Cuidados Primarios')
    #fourth the submit button
    submit = SubmitField('Buscar')

class SearchForm_en(FlaskForm):
    #first start by search type
    search_type = RadioField('Search Type', validators=[validators.DataRequired()], choices=['None', 'City', 'Zip Code'])

    #second the both search types
    city_search = SelectField('City', choices=cities)
    zip_search = StringField('Zip Code', default='00000')
    #third the boolean fields for selcting the serivce type
    dental = BooleanField('Dental Care')
    mental = BooleanField('Mental Health Care')
    primary = BooleanField('Primary Care')
    #fourth the submit button
    submit = SubmitField('Search')
