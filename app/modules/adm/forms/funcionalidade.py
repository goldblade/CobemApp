# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import Form, TextField, validators, fields
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.modules.adm.models.usuario import Modulo
import md5

def enabled_modulos():
	return Modulo.query.filter_by(ativo=True)

class FuncionalidadeForm(Form):
	nome = TextField(u'Nome', [validators.Required()])
	modulo = QuerySelectField(u'Módulo', [validators.Required()], query_factory=enabled_modulos, allow_blank=True)	