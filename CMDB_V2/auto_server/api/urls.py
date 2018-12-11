from django.conf.urls import url
from api import views

urlpatterns = [
    url(r"^asset/$", views.AssetAPI.as_view())
]
