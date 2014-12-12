# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import Form, TextField, validators, fields, BooleanField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class PerfilForm(Form):
	nome = TextField(u'Nome', [validators.Required()])
	ativo = BooleanField(u'Ativo')