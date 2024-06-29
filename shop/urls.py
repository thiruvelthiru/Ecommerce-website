from django.urls import path
from . import views




urlpatterns=[
    path('home',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('collections/',views.collections,name="collections"),
    path('product',views.product,name='product')
]