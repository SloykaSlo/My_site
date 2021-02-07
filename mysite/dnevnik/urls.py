from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'polls'


urlpatterns = [

    path('', views.index, name='index'),
    path('dikt/', TemplateView.as_view(template_name="dnevnik/uroki/dict.html"), name="dikt"),
    path('sit/', TemplateView.as_view(template_name="dnevnik/uroki/set.html"), name="sit"),
    path('taple/', TemplateView.as_view(template_name="dnevnik/uroki/tuple.html"), name="taple"),
    path('liist/', TemplateView.as_view(template_name="dnevnik/uroki/list.html"), name="liist"),
]