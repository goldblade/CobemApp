# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
#from app.modules.auth.controllers import mod
from . import mod
from flask.ext.login import login_required
from flask.ext import login

@mod.route('/funcionalidade')
@mod.route('/funcionalidade/listar')
@mod.route('/funcionalidade/listar/')
@login_required
def funcionalidade_listar_view():
	
	return render_template('adm/funcionalidade/listar.html', active_page='adm', user=login.current_user)