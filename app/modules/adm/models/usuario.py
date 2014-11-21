# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()

'''perfis = db.Table('perfis',
    db.Column('usuario_id', db.Integer, db.ForeignKey('Usuario.id')),
    db.Column('perfil_id', db.Integer, db.ForeignKey('Perfil.id')),
    db.Column('modulo_id', db.Integer, db.ForeignKey('Modulo.id'))
)'''

class Usuario(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	data_cadastro = db.Column(db.DateTime)
	nome = db.Column(db.String(100))
	foto = db.Column(db.String(100))
	email = db.Column(db.String(20), unique=True)
	login = db.Column(db.String(30), unique=True)
	senha = db.Column(db.String(15))	
	ativo = db.Column(db.SmallInteger, default = 1)
	#perfis = db.relationship('Perfil', secondary=perfis, backref=db.backref('usuarios', lazy='dynamic'))

'''class Perfil(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(255))
	ativo = db.Column(db.SmallInteger, default = 0)
'''