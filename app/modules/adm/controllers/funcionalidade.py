# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
#from app.modules.auth.controllers import mod
from . import mod
from flask.ext.login import login_required
from flask.ext import login
from app.models import paginate
from app.modules.adm.models.usuario import Funcionalidade


@mod.route('/funcionalidade', defaults={'page' : 1})
@mod.route('/funcionalidade/listar')
@mod.route('/funcionalidade/listar/<int:page>')
@login_required
def funcionalidade_listar_view(page):
	funcionalidades = Funcionalidade.query.order_by('nome ASC').all()
	res = paginate(funcionalidades, page, Funcionalidade, 8)
	return render_template('adm/funcionalidade/listar.html', active_page='adm', user=login.current_user, **res)

@mod.route('/funcionalidade/adicionar')
@login_required
def funcionalidade_adicionar_view():
	return render_template('adm/funcionalidade/adicionar.html', active_page='adm', user=login.current_user)