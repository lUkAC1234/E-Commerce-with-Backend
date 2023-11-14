# --------------------------------------------------------------------------- #
# Django exceptions
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.db import IntegrityError
from django.db.models import Sum
# --------------------------------------------------------------------------- #
# Trasnlation
from django.utils.translation import gettext_lazy as _


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# Sizes
class SizeModel(models.Model):
    size = models.CharField(max_length=6, verbose_name=_('size'))

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'


# --------------------------------------------------------------------------- #
# Users
class UserModel(AbstractUser):
    user_image = models.ImageField(upload_to='users/%Y/%m/%d/', default='users/userDefaultImage.png', verbose_name=_('user image'))
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('phone'))
    instagram_username = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('instagram username'))
    twitter_username = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('twitter username'))
    github_username = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('github username'))
    telegram_username = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('telegram username'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    bio = models.TextField(max_length=100, null=True, blank=True, verbose_name=_('bio'))


# --------------------------------------------------------------------------- #
# Categories
class CategoryModel(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


# --------------------------------------------------------------------------- #
# Tags
class TagsModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


# --------------------------------------------------------------------------- #
# Colors
class ColorsModel(models.Model):
    name = models.CharField(max_length=7, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


# --------------------------------------------------------------------------- #
# Furniture Model
class FurnitureModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    description = RichTextField()
    short_description = RichTextField()
    image = models.ImageField(upload_to='blogs/%Y/%m/%d/', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))
    categories = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name=_('category'), related_name='products')
    price = models.FloatField(verbose_name=_('price'))
    real_price = models.FloatField(verbose_name=_('real price'), default=0)
    discount = models.PositiveIntegerField(default=0, verbose_name=_('discount'))
    rating = models.PositiveSmallIntegerField(default=1, verbose_name=_('rating'))
    count = models.PositiveIntegerField(default=1, verbose_name=_('count'))
    tags = models.ManyToManyField(TagsModel, verbose_name=_('tag'), related_name='fTags')
    colors = models.ManyToManyField(ColorsModel, verbose_name=_('tag'), related_name='fColors')
    sizes = models.ManyToManyField(SizeModel, verbose_name=_('size'), related_name='fSizes')

    @staticmethod
    def get_cart_objects(cart_list):
        qs = FurnitureModel.objects.all().filter(id__in=cart_list)
        return qs

    @property
    def is_discount(self):
        return self.discount != 0

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'furniture'
        verbose_name_plural = 'furnitures'
        ordering = ('-id',)


# --------------------------------------------------------------------------- #
# Your Wish List Furniture
class WishListModel(models.Model):
    furniture = models.ForeignKey(FurnitureModel, on_delete=models.RESTRICT, related_name='wishlist', verbose_name=_('furniture'))
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='wishlistuser', verbose_name=_('user'))

    def __str__(self):
        return f"{self.furniture} {self.user}"

    @staticmethod
    def create_or_delete(user, furniture):
        try:
            WishListModel.objects.create(user=user, furniture=furniture)
        except IntegrityError:
            WishListModel.objects.get(user=user, furniture=furniture).delete()

    class Meta:
        verbose_name = _('wishlist')
        verbose_name_plural = _('wishlists')
        unique_together = ['user', 'furniture']


# --------------------------------------------------------------------------- #
# Contact Us
class ContactUSModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    email = models.EmailField(max_length=45, verbose_name=_('email'))
    message = models.CharField(max_length=300, verbose_name=_('message'))
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name=_('user'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
        ordering = ('-id',)


# --------------------------------------------------------------------------- #
# FAQ (Frequently Asked Questions) Model
class faqModel(models.Model):
    question = models.CharField(max_length=100, verbose_name=_('question'))
    answer = models.TextField(verbose_name=_('answer'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    class Meta:
        verbose_name = _('faq')
        verbose_name_plural = _('faqs')
        ordering = ('-id',)
# --------------------------------------------------------------------------- #
