# --------------------------------------------------------------------------- #
# Django exceptions
from django.urls import path
# --------------------------------------------------------------------------- #
# Views
from .views import main, aboutus, service, service_single, signup, signin, contactus, order_single, profile, \
    edit, DetailFurniture, contactdelete, contactupdate, faqView, faqCreateView, faqDeleteView, faqUpdateView, \
    wishlist_view, WishListView, cart_view, ShoppingCartView

# --------------------------------------------------------------------------- #
# app_name = 'main'
# main:home

# --------------------------------------------------------------------------- #
# URLS
urlpatterns = [
    path('', main.as_view(), name='main'),
    path('aboutus/', aboutus.as_view(), name='aboutus'),
    path('service/', service.as_view(), name='service'),
    path('servicesingle/', service_single.as_view(), name='service_single'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('contactus/', contactus.as_view(), name='contactus'),
    path('order_single/', order_single.as_view(), name='order_single'),
    path('detail/<int:pk>/', DetailFurniture.as_view(), name='detail'),
    path('profile/', profile.as_view(), name='profile'),
    path('edit/', edit, name='edit'),
    path('faq/', faqView.as_view(), name='faq'),
    path('faqCreateView/', faqCreateView.as_view(), name='faqCreateView'),
    path('faqDeleteView/<int:pk>', faqDeleteView.as_view(), name='faqDeleteView'),
    path('faqUpdateView/<int:pk>', faqUpdateView.as_view(), name='faqUpdateView'),
    path('contactdelete/<int:pk>/', contactdelete.as_view(), name='contactdelete'),
    path('contactupdate/<int:pk>/', contactupdate.as_view(), name='contactupdate'),
    path('wishlist/<int:id>', wishlist_view, name='wishlist'),
    path('wishlist/', WishListView.as_view(), name='wish_list'),
    path('ShoppingCartView/', ShoppingCartView.as_view(), name='ShoppingCartView'),
    path('add_cart/<int:id>/', cart_view, name='add_cart'),
]
# --------------------------------------------------------------------------- #
