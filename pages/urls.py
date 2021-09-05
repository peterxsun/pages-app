from django.urls import path
from .views import HomePagesView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePagesView.as_view(), name='home'),
]