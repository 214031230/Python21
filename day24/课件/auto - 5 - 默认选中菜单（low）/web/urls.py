from django.conf.urls import url,include
from web.views import home

urlpatterns = [
    url(r'^index/', home.index),
    url(r'^user/', home.user),
    url(r'^order/', home.order),
    url(r'^center/', home.center),
]
