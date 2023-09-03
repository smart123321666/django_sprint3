from . import views
from django.urls import path


app_name = 'blog'

urlpatterns = [
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts,
         name='category_posts'),
    path('', views.index, name='index'),
]
