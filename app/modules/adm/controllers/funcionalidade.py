# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
#from app.modules.auth.controllers import mod
from . import mod
from flask.ext.login import login_required
from flask.ext import login
from app.models import paginate
from app.modules.adm.models.usuario import Funcionalidade
from app.modules.adm.forms.funcionalidade import FuncionalidadeForm
from flask.ext.wtf import Form
#from wtforms.ext.appengine.db import model_form
from wtforms.ext.sqlalchemy.orm import model_form
from app import db

@mod.route('/funcionalidade', defaults={'page' : 1})
@mod.route('/funcionalidade/listar')
@mod.route('/funcionalidade/listar/<int:page>')
@login_required
def funcionalidade_listar_view(page):
	funcionalidades = Funcionalidade.query.order_by('nome ASC').all()
	print funcionalidades	
	res = paginate(funcionalidades, page, Funcionalidade, 8)
	return render_template('adm/funcionalidade/listar.html', active_page='adm', user=login.current_user, **res)

@mod.route('/funcionalidade/adicionar', methods=["GET", "POST"])
@login_required
def funcionalidade_adicionar_view():
	form = FuncionalidadeForm(request.form)
	if request.method == 'POST' and form.validate():
		f = Funcionalidade()
		f.nome = form.nome.data
		f.nome_controller = form.nome.data.lower()
		f.modulo_id = form.modulo.data.id
		try:
			db.session.add(f)
			db.session.commit()
		except:
			flash(u'Não foi possível inserir a funcionalidade', 'danger')
		flash(u'Funcionalidade inserida com sucesso!', 'success')
		return redirect(url_for('.funcionalidade_listar_view'))
	return render_template('adm/funcionalidade/adicionar.html', active_page='adm', user=login.current_user, form=form)

@mod.route('/funcionalidade/editar/id/<int:id>', methods=["GET", "POST"])
@login_required
def funcionalidade_editar_view(id):
	try:
		f = Funcionalidade.query.get(id)
	except:
		flash(u'Funcionalidade não encontrada', 'danger')
		return redirect(url_for('.funcionalidade_listar_view'))
	form = FuncionalidadeForm(request.form, obj=f)
	if request.method == 'POST' and form.validate():
		f.nome = form.nome.data
		f.nome_controller = form.nome.data.lower()
		f.modulo_id = form.modulo.data.id
		try:
			db.session.add(f)
			db.session.commit()
		except:
			flash(u'Não foi possível alterar a funcionalidade', 'danger')
		flash(u'Funcionalidade foi alterada com sucesso!', 'success')
		return redirect(url_for('.funcionalidade_listar_view'))

	return render_template('adm/funcionalidade/editar.html', active_page='adm', user=login.current_user, form=form)

@mod.route('/funcionalidade/deletar/id/<int:id>', methods=["GET"])
@login_required
def funcionalidade_deletar_view(id):
	try:
		f = Funcionalidade.query.get(id)
		db.session.delete(f)
		db.session.commit()
		flash(u'Registro removido com sucesso', 'success')
	except:
		flash(u'Registro não encontrado no sistema', 'danger')

	return redirect(url_for('.funcionalidade_listar_view'))

@mod.route('/funcionalidade/exibir/id/<int:id>', methods=["GET"])
@login_required
def funcionalidade_exibir_view(id):
	try:
		f = Funcionalidade.query.get(id)
	except:
		flash(u'Funcionalidade não encontrada!', 'danger')
		return redirect(url_for('.funcionalidade_listar_view'))
	return render_template('adm/funcionalidade/exibir.html', active_page='adm', user=login.current_user, data=f)