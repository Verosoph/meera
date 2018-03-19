from django.conf.urls import url
from django.conf import settings
from .import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^t1',views.thema1),
    url(r'^t1_1',views.thema1_1),
    url(r'^t2',views.thema2),
    url(r'^t3',views.thema3),
    url(r'^t4',views.thema4),

]