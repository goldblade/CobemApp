# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import Form, TextField, validators, fields, BooleanField, PasswordField, FileField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask.ext.wtf.file import FileField, FileRequired, FileAllowed
from app.modules.adm.models.usuario import Perfil

def enabled_perfis():
	return Perfil.query.filter_by(ativo=True)

class UsuarioForm(Form):
	nome = TextField(u'Nome', [validators.Required(), validators.length(max=100)])
	email = TextField(u'Email', [validators.optional(), validators.length(max=100)])
	login = TextField(u'Login', [validators.Required()])
	senha = PasswordField(u'Senha', [validators.Required()])
	ativo = BooleanField(u'Ativo')
	foto = FileField('Foto', validators=[FileAllowed(['jpg', 'png', 'bmp', 'gif'], 'Images only!')])
	perfil = QuerySelectField(u'Perfil', [validators.Required()], query_factory=enabled_perfis, allow_blank=True)