#!/home/jharvard/newDjangoTest/env/bin/python3
# EASY-INSTALL-DEV-SCRIPT: 'Django==1.11.dev20160620182227','django-admin.py'
__requires__ = 'Django==1.11.dev20160620182227'
import sys
from pkg_resources import require
require('Django==1.11.dev20160620182227')
del require
__file__ = '/home/jharvard/newDjangoTest/django/django/bin/django-admin.py'
if sys.version_info < (3, 0):
    execfile(__file__)
else:
    exec(compile(open(__file__).read(), __file__, 'exec'))
