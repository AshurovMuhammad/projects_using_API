from django.urls import path
from .views import weather, deletecity

urlpatterns = [
    path('', weather, name='weather'),
    path('<int:city_pk>/delete/', deletecity, name='deletecity')
]
