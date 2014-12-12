# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import Form, TextField, validators, fields, BooleanField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.modules.adm.models.usuario import Perfil, Funcionalidade
import md5


def enabled_perfil():
	return Perfil.query.filter_by(ativo=True)

def enabled_funcionalidade():
	return Funcionalidade.query

class AcaoForm(Form):	
	perfil = QuerySelectField(u'Perfil', [validators.Required()], query_factory=enabled_perfil, allow_blank=True)
	funcionalidade = QuerySelectField(u'Funcionalidade', [validators.Required()], query_factory=enabled_funcionalidade, allow_blank=True)
	listar = BooleanField(u'Listar')
	adicionar = BooleanField(u'Adicionar')
	editar = BooleanField(u'Editar')
	apagar = BooleanField(u'Apagar')