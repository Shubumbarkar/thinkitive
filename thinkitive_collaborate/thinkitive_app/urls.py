from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('editor/<str:doc_id>/', views.editor, name='editor'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]
