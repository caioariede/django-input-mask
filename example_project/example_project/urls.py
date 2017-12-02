from django.conf.urls import url

from .views import BasicFormView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', BasicFormView.as_view(), name='form'),
]
