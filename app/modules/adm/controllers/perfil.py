# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
from . import mod
from flask.ext.login import login_required
from flask.ext import login
from app.models import paginate
from app.modules.adm.models.usuario import Perfil
from app.modules.adm.forms.perfil import PerfilForm
from flask.ext.wtf import Form
from app import db

@mod.route('/perfil', defaults={'page' : 1})
@mod.route('/perfil/listar')
@mod.route('/perfil/listar/<int:page>')
@login_required
def perfil_listar_view(page):
	perfis = Perfil.query.order_by('nome ASC').all()
	res = paginate(perfis, page, Perfil, 8)
	return render_template('adm/perfil/listar.html', active_page='adm', user=login.current_user, **res)


@mod.route('/perfil/adicionar', methods=["GET", "POST"])
@login_required
def perfil_adicionar_view():
	form = PerfilForm(request.form)
	if request.method == 'POST' and form.validate():
		p = Perfil()
		p.nome = form.nome.data		
		p.ativo = form.ativo.data
		try:
			db.session.add(p)
			db.session.commit()
		except:
			flash(u'Não foi possível inserir o perfil', 'danger')
		flash(u'Perfil inserido com sucesso!', 'success')
		return redirect(url_for('.perfil_listar_view'))
	return render_template('adm/perfil/adicionar.html', active_page='adm', user=login.current_user, form=form)

@mod.route('/perfil/editar/id/<int:id>', methods=["GET", "POST"])
@login_required
def perfil_editar_view(id):    
	try:
		p = Perfil.query.get(id)
	except:
		flash(u'Perfil não encontrado', 'danger')
		return redirect(url_for('.perfil_listar_view'))
	form = PerfilForm(request.form, obj=p)
	if request.method == 'POST' and form.validate():
		p.nome = form.nome.data
		p.ativo = form.ativo.data		
		try:
			db.session.add(p)
			db.session.commit()
		except:
			flash(u'Não foi possível alterar o perfil', 'danger')
		flash(u'Perfil foi alterado com sucesso!', 'success')
		return redirect(url_for('.perfil_listar_view'))
	return render_template('adm/perfil/editar.html', active_page='adm', user=login.current_user, form=form)    

@mod.route('/perfil/deletar/id/<int:id>', methods=["GET"])
@login_required
def perfil_deletar_view(id):    
	try:
		p = Perfil.query.get(id)
		db.session.delete(p)
		db.session.commit()
		flash(u'Registro removido com sucesso', 'success')
	except:
		flash(u'Registro não encontrado no sistema', 'danger')

	return redirect(url_for('.perfil_listar_view'))	    

@mod.route('/perfil/exibir/id/<int:id>', methods=["GET"])
@login_required
def perfil_exibir_view(id):    
	try:
		p = Perfil.query.get(id)
	except:
		flash(u'Perfil não encontrado!', 'danger')
		return redirect(url_for('.perfil_listar_view'))

	return render_template('adm/perfil/exibir.html', active_page='adm', user=login.current_user, data=p)

@mod.route('/perfil/pesquisar', methods=["POST"])
@login_required
def perfil_pesquisar_view():    
	q = request.form['q']
	if request.method == 'POST':
		if q != '':
			busca_perfil = Perfil.query.filter(Perfil.nome.like('%' + q + '%')).all()
		else:
			busca_perfil = Perfil.query.order_by('nome ASC').all()

	return render_template('adm/perfil/pesquisar.html', dados=busca_perfil)