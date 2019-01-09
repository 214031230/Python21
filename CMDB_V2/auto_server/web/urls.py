from django.conf.urls import url
from web import views

urlpatterns = [
    url(r"^test/$", views.test),
]
