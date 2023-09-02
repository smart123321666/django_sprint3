from django.urls import path
from . import views
from .views import AboutView
app_name = 'pages'

urlpatterns = [
    path('pages/about/', AboutView.as_view(), name='about'),
    path('pages/rules/', views.rules, name='rules'),
]
