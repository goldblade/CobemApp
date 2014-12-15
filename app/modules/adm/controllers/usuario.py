# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
#from app.modules.auth.controllers import mod
from . import mod
from flask.ext.login import login_required
from flask.ext import login
from app.modules.adm.models.usuario import Usuario
from app.models import paginate

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
	return 'adicionar'

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