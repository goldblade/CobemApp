# -*- coding: utf-8 -*-
import math

def paginate(query, page, instance, limit):
	result = {}	

	if page <= 0:
		abort(404)

	#num = app.config['NAVIGATION_PAGE_COUNT'] / 2
	#ppp = app.config['POSTS_PER_PAGE']
	num = 8 / 2
	ppp = 8
	try:
		if isinstance(query[0], instance):
			num = limit / 2
			ppp = limit
							
	except IndexError:
		print 'opsss ouve um erro'	

	start = (page - 1) * ppp
	end = start + ppp

	#result['posts'] = query[start:end]	
	result['dados'] = query[start:end]
	#result['max_page'] = max_page = int(math.ceil(query.count() / float(ppp)))
	result['max_page'] = max_page = int(math.ceil(len(query) / float(ppp)))
	result['pages'] = [p for p in xrange(page - num, page + num + 1)
			if 1 < p < max_page]

	return result