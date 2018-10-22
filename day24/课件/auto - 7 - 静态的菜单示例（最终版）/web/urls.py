from django.conf.urls import url,include
from web.views import home

urlpatterns = [
    url(r'^index/', home.index),
    url(r'^user/', home.user),
    url(r'^add_user/', home.add_user),
    url(r'^del_user/(\d+)/', home.del_user),
    url(r'^edit_user/(\d+)/', home.edit_user),

    url(r'^order/', home.order),
    url(r'^center/', home.center),
]
