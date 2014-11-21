# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort
#from app.models import Printer

mod = Blueprint('auth', __name__, url_prefix='/auth')

''' Importando Controllers do Modulo '''
import login
