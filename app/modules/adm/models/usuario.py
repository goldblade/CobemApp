# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime, date
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
#db = SQLAlchemy()

perfis = db.Table('perfis_usuario',
    db.Column('usuario_id', db.Integer, db.ForeignKey('usuario.id')),
    db.Column('perfil_id', db.Integer, db.ForeignKey('perfil.id')),    
)

class Usuario(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	data_cadastro = db.Column(db.DateTime, default = datetime.utcnow())
	nome = db.Column(db.String(100))
	foto = db.Column(db.String(100))
	email = db.Column(db.String(20), unique=True)
	login = db.Column(db.String(30), unique=True)
	senha = db.Column(db.String(15))	
	ativo = db.Column(db.Boolean, default = True)
	perfis = db.relationship('Perfil', secondary=perfis, backref=db.backref('usuarios', lazy='dynamic'))
	def set_senha(self, senha):
		self.senha = generate_password_hash(senha)

	def check_senha(self, senha):
		return check_password_hash(self.senha, senha)
		
	def is_authenticated(self):
		return True	

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id

	def __unicode__(self):
		return self.login

class Modulo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(20))
	ativo = db.Column(db.Boolean, default = True)
	funcionalidade_child = db.relationship("Funcionalidade", cascade="all,delete", backref="postparent")
	def __unicode__(self):
		return self.nome

class Funcionalidade(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(20))
	nome_controller = db.Column(db.String(20))
	modulo_id = db.Column(db.Integer, db.ForeignKey('modulo.id'))	
	modulo = db.relationship("Modulo", backref='funcionalidade', order_by=id)
	def __unicode__(self):
		return self.nome


class Perfil(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(255))	
	ativo = db.Column(db.Boolean, default = True)
	def __unicode__(self):
		return self.nome

class Acao(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	perfil_id = db.Column(db.Integer, db.ForeignKey('perfil.id'))
	perfil = db.relationship("Perfil", backref="acao", order_by=id)
	funcionalidade_id = db.Column(db.Integer, db.ForeignKey('funcionalidade.id'))
	funcionalidade = db.relationship("Funcionalidade", backref="acaofuncionalidade", order_by=id)
	listar = db.Column(db.Boolean, default = False)
	adicionar = db.Column(db.Boolean, default = False)
	editar = db.Column(db.Boolean, default = False)
	apagar = db.Column(db.Boolean, default = False)
