#!/bin/python
user = { 'admin': True, 'active': True, 'name': 'Kevin' }
if user['admin'] and user['active']:
	print("Admin - Active username is %s" % user['name'])
elif user['admin']:
	print("Admin  - User Name is %s" % user['name'])
elif user['active']:
	print("Active - User Name is %s"  % user['name'])
else:
	print("User Name is %s" % user['name'])
