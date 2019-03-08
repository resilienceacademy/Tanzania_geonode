# -*- coding: utf-8 -*-
#

import ast
import os
from urlparse import urlparse, urlunparse
from geonode.settings import *


# Enable email with UTU smtp
EMAIL_ENABLE = True

# dummy values - change before using!
if EMAIL_ENABLE:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'internal-email-host-url'
    EMAIL_PORT = internal-email-port-integer
    EMAIL_HOST_USER = 'internal-email-user'
    EMAIL_HOST_PASSWORD = 'internal-email-password'
    EMAIL_USE_TLS = internal-email-use-tls-boolean
    DEFAULT_FROM_EMAIL = 'UTU Geonode <no-reply@utu.fi>'
