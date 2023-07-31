from django.urls import path
from django.contrib.auth import views

from core.views import frontpage, shop, signup, my_account, edit_my_account

from product.views import product

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>', product, name='product'),
    path('myaccount/', my_account, name='my_account'),
    path('editaccount/', edit_my_account, name='edit_account'),
]