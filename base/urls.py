from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('products/<int:pk>',views.products,name='products'),
    path('create-product/',views.createProduct,name='create-product'),
    path('update-product/<int:pk>',views.updateProduct,name='update-product'),
    path('delete-product/<int:pk>',views.deleteProduct,name='delete-product'),
    path('login/',views.loginPge,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('chat/<int:pk>',views.Chatt,name='chat'),
    path('delete-message/<int:pk>',views.deleteMessage,name='delete-message'),
    path('profile/<int:pk>',views.userProfile,name='profile'),





    
]

