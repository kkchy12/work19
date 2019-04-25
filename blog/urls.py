from django.urls import path
from blog import views

app_name = 'blog'  ## 이 부분 누락되지 않도록 주의!!!

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
]