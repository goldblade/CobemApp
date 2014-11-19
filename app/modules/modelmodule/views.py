from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

mod = Blueprint('modelmodule', __name__, url_prefix='/modelmodule')

@mod.route('/me/')
def home():
	return "Carregou o home do modulo"