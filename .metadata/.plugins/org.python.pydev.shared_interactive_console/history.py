import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'ScrumWeb.settings'; import django
if django.get_version() < '1.5':
    from django.core import management
    import ScrumWeb.settings as settings
    management.setup_environ(settings)
if django.get_version() >= '1.7':
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
exit
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'ScrumWeb.settings'; import django
if django.get_version() < '1.5':
    from django.core import management
    import ScrumWeb.settings as settings
    management.setup_environ(settings)
if django.get_version() >= '1.7':
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'ScrumWeb.settings'; import django
if django.get_version() < '1.5':
    from django.core import management
    import ScrumWeb.settings as settings
    management.setup_environ(settings)
if django.get_version() >= '1.7':
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
from django.contrib.auth.models import User
User.objects.all()
usuario = User.objects.create_superuser('Scrum Master', 'jumisanbeg@gmail.com', 'scrummaster')
User.objects.all()
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
