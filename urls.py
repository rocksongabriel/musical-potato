# -*- coding: utf-8 -*-
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls
from django.urls import path, include


urlpatterns = [
    # add your own patterns here
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
