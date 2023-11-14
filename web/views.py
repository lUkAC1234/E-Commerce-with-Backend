# --------------------------------------------------------------------------- #
# Django exceptions
from captcha.fields import CaptchaField
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.db.models import Min, Max
# --------------------------------------------------------------------------- #

# Models and Forms  
# --------------------------------------------------------------------------- #
from .models import FurnitureModel, UserModel, CategoryModel, ContactUSModel, TagsModel, ColorsModel, SizeModel, \
    faqModel, WishListModel
from .forms import AccountForm, FurnitureModelForm, RegistrationForm, LoginForm, ContactModelForm, faqModelForm
# --------------------------------------------------------------------------- #

# Generic Classes
# --------------------------------------------------------------------------- #
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# views
# --------------------------------------------------------------------------- #
# Main View
class main(TemplateView):
    template_name = 'pages/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['furniture'] = FurnitureModel.objects.all().order_by('-id')[:3]
        data['experience'] = FurnitureModel.objects.all()
        data['user'] = UserModel.objects.all()
        return data


# --------------------------------------------------------------------------- #
# About us view
class aboutus(CreateView):
    form_class = ContactModelForm
    template_name = 'pages/about.html'
    success_url = '/contactus'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(aboutus, self).form_valid(form)


# --------------------------------------------------------------------------- #
# Service View
class service(TemplateView):
    template_name = 'pages/services.html'


# --------------------------------------------------------------------------- #
# Service single View
class service_single(TemplateView):
    template_name = 'pages/service_single.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['experience'] = FurnitureModel.objects.all()
        data['user'] = UserModel.objects.all()
        return data


# --------------------------------------------------------------------------- #
# FAQ (Frequently Asked Questions) List View
class faqView(ListView):
    model = faqModel
    template_name = 'pages/faq.html'


# --------------------------------------------------------------------------- #
# FAQ (Frequently Asked Questions) Create View
class faqCreateView(LoginRequiredMixin, CreateView):
    form_class = faqModelForm
    template_name = 'pages/faqCreateView.html'
    success_url = '/faq'


# --------------------------------------------------------------------------- #
# FAQ (Frequently Asked Questions) Delete View
class faqDeleteView(LoginRequiredMixin, DeleteView):
    model = faqModel
    template_name = 'pages/faqDelete.html'
    success_url = '/faq'


# --------------------------------------------------------------------------- #
# FAQ (Frequently Asked Questions) Update View
class faqUpdateView(LoginRequiredMixin, UpdateView):
    model = faqModel
    form_class = faqModelForm
    template_name = 'pages/faqUpdate.html'
    success_url = '/faq'


# --------------------------------------------------------------------------- #
# Ordering
class order_single(ListView):
    template_name = 'pages/order-single.html'

    def get_queryset(self):
        furnitures = FurnitureModel.objects.all()
        tag = self.request.GET.get('tag', '')
        search = self.request.GET.get('search', '')
        category = self.request.GET.get('category', '')
        size_q = self.request.GET.get('size_q', '')
        color_q = self.request.GET.get('color_q', '')
        price = self.request.GET.get('price', '')
        if search: furnitures = furnitures.filter(Q(title__icontains=search) | Q(categories__name__icontains=search))
        if tag and tag.isdigit():
            tmp = FurnitureModel.objects.all().filter(id=tag).exists()
            if tmp:
                furnitures = furnitures.filter(tags=tag)
        if category and category.isdigit():
            tmp = FurnitureModel.objects.all().filter(id=category).exists()
            if tmp:
                furnitures = furnitures.filter(categories=category)
        if size_q and size_q.isdigit():
            tmp = FurnitureModel.objects.all().filter(id=size_q).exists()
            if tmp:
                furnitures = furnitures.filter(sizes=size_q)
        if color_q and color_q.isdigit():
            tmp = FurnitureModel.objects.all().filter(id=color_q).exists()
            if tmp:
                furnitures = furnitures.filter(colors=color_q)
        if price:
            min_price, max_price = price.split(';')
            furnitures = furnitures.filter(real_price__gte=min_price, real_price__lte=max_price)
        return furnitures

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        tag = self.request.GET.get('tag', '')
        if tag and tag.isdigit():
            tmp = FurnitureModel.objects.all().filter(id=tag).exists()
            if tmp:
                data['tag'] = TagsModel.objects.get(id=tag)
        data['tags'] = TagsModel.objects.all()
        data['colors'] = ColorsModel.objects.all()
        data['sizes'] = SizeModel.objects.all()
        data['categories'] = CategoryModel.objects.all()
        data['min'], data['max'] = FurnitureModel.objects.all().aggregate(Min('real_price'), Max('real_price')).values()
        return data


# --------------------------------------------------------------------------- #
# Furniture Detail View
class DetailFurniture(DetailView):
    model = FurnitureModel
    template_name = 'pages/furniture-detail.html'


# --------------------------------------------------------------------------- #
# Registration View
def signup(request):
    if request.user.is_authenticated:
        raise ValidationError('You are already authenticated please logout and then try again.')
    else:
        request.title = 'Interno - Sign Up'
        template_name = 'pages/signup.html'
        form_registration = RegistrationForm()
        if request.method == 'POST':
            form_registration = RegistrationForm(data=request.POST, files=request.FILES)
            if form_registration.is_valid():
                del form_registration.cleaned_data['confirm_password']
                user_registration = UserModel(
                    username=form_registration.cleaned_data['username'],
                    password=make_password(form_registration.cleaned_data['password']),
                    email=form_registration.cleaned_data['email']
                )
                user_registration.save()
                return redirect('signin')
            # raise ValidationError(form_registration.errors)

        return render(request, template_name, context={
            'form': form_registration
        })


# --------------------------------------------------------------------------- #
# Login View
def signin(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('main')
    else:
        request.title = 'Interno - Sign In'
        template_name = 'pages/signin.html'
        form_login = LoginForm()
        if request.method == 'POST':
            form_login = LoginForm(data=request.POST)
            if form_login.is_valid():
                user_login = authenticate(
                    username=form_login.cleaned_data['username'],
                    password=form_login.cleaned_data['password']
                )
                if user_login is not None:
                    login(request, user_login)
                    return redirect('main')
                form_login.add_error('password', 'Username or password is incorrect')

        return render(request, template_name, context={
            'form': form_login
        })


# --------------------------------------------------------------------------- #
# Contact us View
class contactus(LoginRequiredMixin, CreateView):
    form_class = ContactModelForm
    template_name = 'pages/contact.html'

    def get_success_url(self):
        return reverse('contactus')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(contactus, self).form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['contact'] = ContactUSModel.objects.all().filter(user=self.request.user)
        data['contact_admin'] = ContactUSModel.objects.all()
        return data


# --------------------------------------------------------------------------- #
# Contact us Update View
class contactupdate(LoginRequiredMixin, UpdateView):
    model = ContactUSModel
    form_class = ContactModelForm
    template_name = 'pages/contact-update.html'
    success_url = '/contactus'


# --------------------------------------------------------------------------- #
# Contact us Delete View
class contactdelete(LoginRequiredMixin, DeleteView):
    model = ContactUSModel
    template_name = 'pages/contact-delete.html'
    success_url = '/contactus'


# --------------------------------------------------------------------------- #
# Profile View
class profile(LoginRequiredMixin, TemplateView):
    template_name = 'pages/profile.html'


# --------------------------------------------------------------------------- #
# Edit profile View
@login_required()
def edit(request):
    form = AccountForm
    template_name = 'pages/edit.html'
    if request.method == 'POST':
        form = AccountForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            user = get_object_or_404(UserModel, id=request.user.id)
            form.save()
            return redirect('profile')
    return render(request, template_name)


# --------------------------------------------------------------------------- #
# Wish List
def wishlist_view(request, id):
    furniture = FurnitureModel.objects.get(id=id)
    WishListModel.create_or_delete(request.user, furniture)
    path = request.GET.get('path', '')
    return redirect(path)


# --------------------------------------------------------------------------- #
# List of furniture that user added to favourites
class WishListView(LoginRequiredMixin, ListView):
    template_name = 'pages/wishlist.html'

    def get_queryset(self):
        qs = WishListModel.objects.all().filter(user=self.request.user)
        return qs


# --------------------------------------------------------------------------- #
# Cart View
def cart_view(request, id):
    cart = request.session.get('cart', [])

    if not cart:
        request.session['cart'] = []
        cart = request.session.get('cart', [])
    if id in cart:
        cart.remove(id)
    else:
        cart.append(id)

    request.session['cart'] = cart
    path = request.GET.get('next', '/')
    print(cart)

    return redirect(path)


# --------------------------------------------------------------------------- #
# Shopping Cart View
class ShoppingCartView(LoginRequiredMixin, ListView):
    template_name = 'pages/shopping-cart.html'

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        qs = FurnitureModel.get_cart_objects(cart)
        return qs

# --------------------------------------------------------------------------- #
