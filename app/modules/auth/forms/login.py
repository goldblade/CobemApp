# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import Form, TextField, validators, TextAreaField, fields, PasswordField, SelectField, FileField
from flask.ext.wtf.file import FileField, FileRequired, FileAllowed
from app.modules.adm.models.usuario import Usuario
from app import db
import md5

class LoginForm(Form):
	login = TextField(u'Login', [validators.Required()])
	senha = PasswordField(u'Senha', [validators.Required()])
	def validate_login(self, field):
		user = self.get_user()		
		if user is None:			
			raise validators.ValidationError(u'Usuário e\ou Senha Inválidos')		
		if not user.check_senha(self.senha.data):
			raise validators.ValidationError(u'Usuário e\ou Senha Inválidos')
	def get_user(self):
		return db.session.query(Usuario).filter_by(login=self.login.data).first()