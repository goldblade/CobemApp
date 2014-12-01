# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, url_for
from flask.ext.login import LoginManager, login_required
from flask.ext import login
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babel import Babel, lazy_gettext, gettext, refresh, ngettext
#import app.modules.usuario.models
#import app.modules.usuario.controller

app = Flask(__name__)
app.config.from_object('config')
app.config['BABEL_DEFAULT_LOCALE'] = 'pt_BR'
""" Translate """
babel = Babel(app)
db = SQLAlchemy()
db.init_app(app)

@app.route('/')
@app.route('/index.html')
@login_required
def inicio():
  return render_template('index.html', user=login.current_user)


@app.route('/teamunifacs')
def team_unifacs_view():
	membros = [
		('eduardo.jpg', u'Eduardo Júnior', u'Analista e Desenvolvedor', u'Irecê - BA', u'ej@eduardojunior.com', 
			'(74) 9932-6161'),
		('robert-300.jpg', u'Eduardo Júnior', u'Analista e Desenvolvedor', u'Irecê - BA', u'ej@eduardojunior.com', 
			'(74) 9932-6161'),
		('robert-300.jpg', u'Eduardo Júnior', u'Analista e Desenvolvedor', u'Irecê - BA', u'ej@eduardojunior.com', 
			'(74) 9932-6161'),
		('robert-300.jpg', u'Eduardo Júnior', u'Analista e Desenvolvedor', u'Irecê - BA', u'ej@eduardojunior.com', 
			'(74) 9932-6161'),
		('robert-300.jpg', u'Eduardo Júnior', u'Analista e Desenvolvedor', u'Irecê - BA', u'ej@eduardojunior.com', 
			'(74) 9932-6161'),
		('robert-300.jpg', u'Eduardo Júnior', u'Analista e Desenvolvedor', u'Irecê - BA', u'ej@eduardojunior.com', 
			'(74) 9932-6161'),
	]		
	return render_template('teamunifacs.html', membros=membros, user=login.current_user)

@app.route('/install')
def install():
	db.drop_all()
	db.create_all()	
	from app.modules.adm.models.usuario import Usuario, Modulo
	usuario = Usuario()
	usuario.nome = 'admin'
	usuario.login = 'admin'
	usuario.set_senha('admin')
	db.session.add(usuario)

	modulos = [
		'adm',
	]
	for m in modulos:
		mod = Modulo()
		mod.nome = m
		db.session.add(mod)

	db.session.commit()

	return "install..."

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.modules.modelmodule.views import mod as modelmoduleModule
app.register_blueprint(modelmoduleModule)

from app.modules.adm.controllers import mod as modulo_adm
app.register_blueprint(modulo_adm)

from app.modules.auth.controllers import mod as modulo_auth
app.register_blueprint(modulo_auth)

def init_login():
	from app.modules.adm.models.usuario import Usuario
	login_manager = login.LoginManager()
	login_manager.setup_app(app)
	# Create user loader function
	@login_manager.user_loader
	def load_user(user_id):
		return db.session.query(Usuario).get(user_id)

	@login_manager.unauthorized_handler
	def unauthorized():
		''' redirecionar para tela de login '''		
		return redirect(url_for('auth.login_view'))


""" INICIANDO LOGIN """
init_login()

# Later on you'll import the other blueprints the same way:
#from app.comments.views import mod as commentsModule
#from app.posts.views import mod as postsModule
#app.register_blueprint(commentsModule)
#app.register_blueprint(postsModule)