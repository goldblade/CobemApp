# -*- coding: utf-8 -*-
from flask import Flask, render_template
#import app.modules.usuario.models
#import app.modules.usuario.controller

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
@app.route('/index.html')
def inicio():
  return render_template('index.html')


@app.route('/teamunifacs')
def team_unifacs_view():
	membros = [
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
		('robert-300.jpg', u'Eduardo Júnior', u'Analista e Desenvolvedor', u'Irecê - BA', u'ej@eduardojunior.com', 
			'(74) 9932-6161'),
	]		
	return render_template('teamunifacs.html', membros=membros)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.modules.modelmodule.views import mod as modelmoduleModule
app.register_blueprint(modelmoduleModule)

from app.modules.adm.controllers import mod as modulo_adm
app.register_blueprint(modulo_adm)

from app.modules.auth.controllers import mod as modulo_auth
app.register_blueprint(modulo_auth)

# Later on you'll import the other blueprints the same way:
#from app.comments.views import mod as commentsModule
#from app.posts.views import mod as postsModule
#app.register_blueprint(commentsModule)
#app.register_blueprint(postsModule)