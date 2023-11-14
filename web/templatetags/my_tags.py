# --------------------------------------------------------------------------- #
# Django exceptions
from django import template
from django.db.models import Sum

# --------------------------------------------------------------------------- #
# Models
from web.models import FurnitureModel, WishListModel

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
register = template.Library()


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# WishList Tag
@register.simple_tag
def is_wishlist(request, id):
    furniture = FurnitureModel.objects.get(id=id)
    return WishListModel.objects.all().filter(user=request.user, furniture=furniture).exists()


# --------------------------------------------------------------------------- #
# Cart Tag
@register.simple_tag
def cart_info(request):
    cart = request.session.get('cart', [])
    qs = FurnitureModel.get_cart_objects(cart)
    if not qs: price = 0.0
    else: price = qs.aggregate(Sum('real_price'))['real_price__sum']
    return len(cart), price
# --------------------------------------------------------------------------- #
# Is Cart ?
@register.simple_tag
def is_cart(request, id):
    cart = request.session.get('cart', [])
    return id in cart
# --------------------------------------------------------------------------- #