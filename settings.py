# This is a fairly standard Django settings file, with some special additions
# that allow addon applications to auto-configure themselves. If it looks 
# unfamiliar, please see our documentation:
#
#   http://docs.divio.com/en/latest/reference/configuration-settings-file.html
#
# and comments below.
import os

from django.urls.base import reverse_lazy


# INSTALLED_ADDONS is a list of self-configuring Divio Cloud addons - see the
# Addons view in your project's dashboard. See also the addons directory in 
# this project, and the INSTALLED_ADDONS section in requirements.in.

INSTALLED_ADDONS = [
    # Important: Items listed inside the next block are auto-generated.
    # Manual changes will be overwritten.

    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    # </INSTALLED_ADDONS>
]

# Now we will load auto-configured settings for addons. See:
#
#   http://docs.divio.com/en/latest/reference/configuration-aldryn-config.html
#
# for information about how this works.
#
# Note that any settings you provide before the next two lines are liable to be
# overwritten, so they should be placed *after* this section.

import aldryn_addons.settings
aldryn_addons.settings.load(locals())

# Your own Django settings can be applied from here on. Key settings like
# INSTALLED_APPS, MIDDLEWARE and TEMPLATES are provided in the Aldryn Django
# addon. See:
#
#   http://docs.divio.com/en/latest/how-to/configure-settings.html
#
# for guidance on managing these settings.

INSTALLED_APPS.extend([
    # Extend the INSTALLED_APPS setting by listing additional applications here
    "django.contrib.postgres",

    # 3rd party applications
    "django_extensions",

    # developer created apps
    "users",
    "vote_app",
])

# INSTALLED_APPS.insert(0, "grappelli")

# To see the settings that have been applied, use the Django diffsettings 
# management command. 
# See https://docs.divio.com/en/latest/how-to/configure-settings.html#list

AUTH_USER_MODEL = "users.User"

# Grapelli settings
GRAPPELLI_ADMIN_TITLE = "Voting Platform"
GRAPPELLI_SWITCH_USER = "True"

# Media settings
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join('/data/media/')

SITE_ID = 1

LOGIN_REDIRECT_URL = reverse_lazy("vote_app:vote-categories")
LOGOUT_REDIRECT_URL = reverse_lazy("pages:home")