from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('signup/', views.signup, name='signup'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('save-for-later/<int:product_id>/', views.save_for_later, name='save_for_later'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('process-order/', views.process_order, name='process_order'),
    path('search/', views.search, name='search'),
    path('recommendations/<int:product_id>/', views.recommendations, name='recommendations'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.custom_logout, name='logout'),
]
