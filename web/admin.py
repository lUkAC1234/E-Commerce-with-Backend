# --------------------------------------------------------------------------- #
# Django exceptions
from django.contrib import admin
# --------------------------------------------------------------------------- #
# Models and Forms
from .models import UserModel, CategoryModel, FurnitureModel, ContactUSModel, TagsModel, ColorsModel, SizeModel, faqModel
from .forms import ColorForm
# --------------------------------------------------------------------------- #
# Translation
from django.utils.translation import gettext_lazy as _
# --------------------------------------------------------------------------- #
# For saving html code
from django.utils.safestring import mark_safe


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# User Model Admin
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['id', 'username']
    search_fields = ['username']


# --------------------------------------------------------------------------- #
# Contact Model Admin
@admin.register(ContactUSModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


# --------------------------------------------------------------------------- #
# FAQ (Frequently Asked Questions) Model Admin
@admin.register(faqModel)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']
    list_display_links = ['id', 'question']
    search_fields = ['question']


# --------------------------------------------------------------------------- #
# Tags Model Admin
@admin.register(TagsModel)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


# --------------------------------------------------------------------------- #
# Sizes Model Admin
@admin.register(SizeModel)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'size']
    list_display_links = ['id', 'size']
    search_fields = ['size']


# --------------------------------------------------------------------------- #
# Colors Model Admin
@admin.register(ColorsModel)
class ColorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'color']
    list_display_links = ['id', 'name', 'color']
    search_fields = ['name']
    form = ColorForm

    def color(self, obj):
        return mark_safe(
            f"<div style='background-color: {obj.name}; width: 30px; height: 30px; border-radius: 50%; box-shadow: 0 5px 10px rgb(0 0 0 / 20%);'></div>")


# --------------------------------------------------------------------------- #
# Furniture Model Admin
@admin.register(FurnitureModel)
class FurnitureModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['created_at']
    fields = ['title', 'short_description', 'description', 'image', 'get_photo', 'categories', 'price', 'discount',
              'real_price', 'rating', 'count', 'tags', 'colors',
              'sizes', 'created_at', 'updated_at']
    readonly_fields = ['real_price', 'created_at', 'updated_at', 'get_photo']

    def get_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=100>")

    get_photo.short_description = 'Image'


# --------------------------------------------------------------------------- #
# Category Model Admin
@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


# --------------------------------------------------------------------------- #
# Admin Site header text
admin.site.site_header = 'Interno Administration'
admin.site.site_title = 'Interno Administration'
# --------------------------------------------------------------------------- #
