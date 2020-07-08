from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:url>/', views.redirect_view, name='redirect'),
]