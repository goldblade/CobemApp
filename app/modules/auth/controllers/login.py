# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
#from app.modules.auth.controllers import mod
from . import mod
from app.modules.auth.forms.login import LoginForm
from flask.ext import login
from flask.ext.login import login_required

@mod.route('/login', methods=('GET', 'POST'))
@mod.route('/login/', methods=('GET', 'POST'))
def login_view():	
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		user = form.get_user()
		login.login_user(user)
		return redirect('/')
	return render_template('auth/login/login.html', active_page='login', form=form)

@mod.route('/logout')
@mod.route('/logout/')
@login_required
def logout_view():
	login.logout_user()
	return redirect(url_for('.login_view'))