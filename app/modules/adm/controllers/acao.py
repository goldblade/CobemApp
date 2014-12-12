# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
from . import mod
from flask.ext.login import login_required
from flask.ext import login
from sqlalchemy.orm import aliased
from app.models import paginate
from app.modules.adm.models.usuario import Acao, Perfil
from app.modules.adm.forms.acao import AcaoForm
from flask.ext.wtf import Form
from app import db

@mod.route('/acao', defaults={'page' : 1})
@mod.route('/acao/listar')
@mod.route('/acao/listar/<int:page>')
@login_required
def acao_listar_view(page):
	acoes = Acao.query.order_by('perfil_id ASC').all()
	res = paginate(acoes, page, Acao, 8)
	return render_template('adm/acao/listar.html', active_page='adm', user=login.current_user, **res)


@mod.route('/acao/adicionar', methods=["GET", "POST"])
@login_required
def acao_adicionar_view():
	form = AcaoForm(request.form)
	if request.method == 'POST' and form.validate():		
		a = Acao()
		a.perfil_id = form.perfil.data.id
		a.funcionalidade_id = form.funcionalidade.data.id
		a.listar = form.listar.data
		a.adicionar = form.adicionar.data
		a.editar = form.editar.data
		a.apagar = form.apagar.data
		try:
			db.session.add(a)
			db.session.commit()
		except:
			flash(u'Não foi possível inserir a ação', 'danger')
		flash(u'Ação inserida com sucesso!', 'success')
		return redirect(url_for('.acao_listar_view'))
	return render_template('adm/acao/adicionar.html', active_page='adm', user=login.current_user, form=form)

@mod.route('/acao/editar/id/<int:id>', methods=["GET", "POST"])
@login_required
def acao_editar_view(id):    
	try:
		a = Acao.query.get(id)
	except:
		flash(u'Ação não encontrada', 'danger')
		return redirect(url_for('.acao_listar_view'))
	form = AcaoForm(request.form, obj=a)
	if request.method == 'POST' and form.validate():
		a.perfil_id = form.perfil.data.id
		a.funcionalidade_id = form.funcionalidade.data.id
		a.listar = form.listar.data
		a.adicionar = form.adicionar.data
		a.editar = form.editar.data
		a.apagar = form.apagar.data
		try:
			db.session.add(a)
			db.session.commit()
		except:
			flash(u'Não foi possível alterar a ação', 'danger')
		flash(u'Ação foi alterada com sucesso!', 'success')
		return redirect(url_for('.acao_listar_view'))
	return render_template('adm/acao/editar.html', active_page='adm', user=login.current_user, form=form) 

@mod.route('/acao/deletar/id/<int:id>', methods=["GET"])
@login_required
def acao_deletar_view(id):    
	try:
		a = Acao.query.get(id)
		db.session.delete(a)
		db.session.commit()
		flash(u'Registro removido com sucesso', 'success')
	except:
		flash(u'Registro não encontrado no sistema', 'danger')

	return redirect(url_for('.acao_listar_view'))

@mod.route('/acao/exibir/id/<int:id>', methods=["GET"])
@login_required
def acao_exibir_view(id):
	try:
		a = Acao.query.get(id)
	except:
		flash(u'Ação não encontrada!', 'danger')
		return redirect(url_for('.acao_listar_view'))
	return render_template('adm/acao/exibir.html', active_page='adm', user=login.current_user, data=a)

@mod.route('/acao/pesquisar', methods=["POST"])
@login_required
def acao_pesquisar_view():
	q = request.form['q']	
	if request.method == 'POST':		
		if q != '':
			parent = aliased(Perfil)
			busca = Acao.query.join(parent, Acao.perfil).filter(parent.nome.like('%' + q + '%')).all()
		else:
			busca = Acao.query.order_by('perfil_id ASC').all()

	return render_template('adm/acao/pesquisar.html', dados=busca)