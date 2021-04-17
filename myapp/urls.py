from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.sample1, name="sample1"),
    path('sample2/', views.sample2, name="sample2"),
]
