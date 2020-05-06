
from django.urls import path,include
from . import views

alpha = ""
urlpatterns = [
    path('bilgilendirme/', views.bilgilendirme, name="bilgilendirme"),
    path('dunya/', views.dunya , name="dunya"),
    path('ulke/', views.ulke , name="ulke"),
    # path('ulkeler<str:alpha>', views.ulkeler)
]
