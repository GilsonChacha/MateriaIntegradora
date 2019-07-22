import os
import sys
import django
import datetime
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tracking.settings')
django.setup()

from django.contrib.auth.models import User
user_c = User.objects.create_superuser(username="administrador",
                                       email="administrador@hotmail.com",
                                       password="a1234567890",
                                       first_name="administrador",
                                       last_name="administrador",
                                       is_active=True)
