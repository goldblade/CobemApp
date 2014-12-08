# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
from . import mod
from flask.ext.login import login_required
from flask.ext import login
from app.models import paginate
from app.modules.adm.models.usuario import Acao
#from app.modules.adm.forms.funcionalidade import FuncionalidadeForm
from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form
from app import db

@mod.route('/acao', defaults={'page' : 1})
@mod.route('/acao/listar')
@mod.route('/acao/listar/<int:page>')
@login_required
def acao_listar_view(page):
	acoes = Acao.query.order_by('id').all()
	res = paginate(acoes, page, Acao, 8)
	return render_template('adm/acao/listar.html', active_page='adm', user=login.current_user, **res)