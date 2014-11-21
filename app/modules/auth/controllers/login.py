# -*- coding: utf-8 -*-
from flask import render_template, request
#from app.modules.auth.controllers import mod
from . import mod

@mod.route('/login', methods=('GET', 'POST'))
@mod.route('/login/', methods=('GET', 'POST'))
def login_view():	
	return render_template('auth/login/login.html')