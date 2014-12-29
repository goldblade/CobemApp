# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
#from app.modules.auth.controllers import mod
from . import mod
from flask.ext.login import login_required
from flask.ext import login
from app.modules.adm.models.usuario import Usuario
from app.modules.adm.forms.usuario import UsuarioForm
from app.models import paginate
from app import db


@mod.route('/usuario', defaults={'page' : 1})
@mod.route('/usuario/listar')
@mod.route('/usuario/listar/<int:page>')
@login_required
def usuario_listar_view(page):
	usuarios = Usuario.query.order_by('nome ASC').all()
	res = paginate(usuarios, page, Usuario, 8)
	return render_template('adm/usuario/listar.html', active_page='adm', user=login.current_user, **res)

@mod.route('/usuario/adicionar', methods=["GET", "POST"])
@login_required
def usuario_adicionar_view():
	form = UsuarioForm(request.form)
	if request.method == 'POST' and form.validate():

		u = Usuario()
		u.login = form.login.data
		u.ativo = form.ativo.data
		u.email = form.email.data
		u.foto = form.foto.data
		u.set_senha(form.senha.data)
		u.nome = form.nome.data
		u.perfis = [form.perfil.data]

		try:

			db.session.add(u)
			db.session.commit()

		except:

			flash(u'Não foi possível inserir o usuário', 'danger')

		flash(u'Usuário Inserido com sucesso!', 'success')

		return redirect(url_for('.usuario_listar_view'))

	return render_template('adm/usuario/adicionar.html', active_page='adm', user=login.current_user, form=form)

@mod.route('/usuario/editar/id/<int:id>', methods=["GET", "POST"])
@login_required
def usuario_editar_view(id):
	return 'editar'


@mod.route('/usuario/deletar/id/<int:id>', methods=["GET"])
@login_required
def usuario_deletar_view(id):
	return 'deletar'

@mod.route('/usuario/exibir/id/<int:id>', methods=["GET"])
@login_required
def usuario_exibir_view(id):
	return 'exibir'

@mod.route('/usuario/pesquisar', methods=["POST"])
@login_required
def usuario_pesquisar_view():
	return 'pesquisar'