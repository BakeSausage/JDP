from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('upload/', views.upload_file, name='upload_file'),
    path('scores/', views.view_scores, name='view_scores'),
]
