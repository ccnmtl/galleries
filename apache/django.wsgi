import os, sys, site

# enable the virtualenv
site.addsitedir('/var/www/galleries/galleries/ve/lib/python2.7/site-packages')

# paths we might need to pick up the project's settings
sys.path.append('/var/www/galleries/galleries/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'galleries.settings_production'

import django
django.setup()

import django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
