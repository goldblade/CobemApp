from flask import Blueprint, render_template, abort

#from project import app
#from project.models import Printer
#from flask import render_template
#import project.controller.printer


mod = Blueprint('usuario', __name__, url_prefix='/usuario')

@mod.route('/me/')
def home():
	return "Carregou o home do modulo usuario"