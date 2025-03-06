from django.urls import path

from .views import home, contato, produto

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
]