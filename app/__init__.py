# -*- coding: utf-8 -*-
from flask import Flask
#import app.modules.usuario.models
#import app.modules.usuario.controller

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def inicio():
  return "CARREGOU O INICIO DA APLICACAO"

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.modules.modelmodule.views import mod as modelmoduleModule
app.register_blueprint(modelmoduleModule)

from app.modules.usuario.controllers import mod as modulo_usuario
app.register_blueprint(modulo_usuario)

# Later on you'll import the other blueprints the same way:
#from app.comments.views import mod as commentsModule
#from app.posts.views import mod as postsModule
#app.register_blueprint(commentsModule)
#app.register_blueprint(postsModule)