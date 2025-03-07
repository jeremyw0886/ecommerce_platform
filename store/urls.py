from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('save-for-later/<int:product_id>/', views.save_for_later, name='save_for_later'),
    path('update-cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('saved/move/<int:saved_item_id>/', views.move_to_cart, name='move_to_cart'),
    path('saved/remove/<int:saved_item_id>/', views.remove_saved_item, name='remove_saved_item'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('process-order/', views.process_order, name='process_order'),
    path('search/', views.search, name='search'),
    path('recommendations/<int:product_id>/', views.recommendations, name='recommendations'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.custom_logout, name='logout'),
]
