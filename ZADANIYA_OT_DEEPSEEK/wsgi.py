"""
WSGI config for ZADANIYA_OT_DEEPSEEK project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZADANIYA_OT_DEEPSEEK.settings')

application = get_wsgi_application()
