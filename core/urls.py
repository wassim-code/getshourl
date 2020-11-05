from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:url_pk>/', views.RedirectView.as_view(), name='redirect'),
    path('<str:pk>/total-clicks/', views.UrlDetailView.as_view(), name='url_detail'),
]