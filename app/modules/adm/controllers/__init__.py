# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort


mod = Blueprint('adm', __name__, url_prefix='/adm')
''' Importando Controllers do Modulo '''
import usuario, funcionalidade, perfil, acao