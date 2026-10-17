from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from .models import *


def home_view(request):
    """Bosh sahifa: toifalar va sara mahsulotlar"""
    categories = Category.objects.annotate(item_count=Count('products'))
    trending_products = Product.objects.filter(is_available=True)[:8]

    context = {
        'featured_categories': categories,
        'categories_preview': categories,
        'trending_products': trending_products,
    }
    return render(request, 'home.html', context)


def products_view(request):
    """Mahsulotlar katalogi: qidiruv, toifa filtri va sahifalash (Paginator)"""
    categories = Category.objects.annotate(item_count=Count('products'))
    products_list = Product.objects.filter(is_available=True)

    category_slug = request.GET.get('category')
    if category_slug:
        products_list = products_list.filter(category__slug=category_slug)

    query = request.GET.get('q')
    if query:
        products_list = products_list.filter(name__icontains=query)

    paginator = Paginator(products_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'categories_preview': categories,
        'products': page_obj,
        'page_obj': page_obj,
        'selected_category': category_slug,
    }
    return render(request, 'products.html', context)


def product_detail_view(request, slug):
    """Mahsulot tafsilotlari sahifasi"""
    product = get_object_or_404(Product, slug=slug, is_available=True)
    related_products = Product.objects.filter(
        category=product.category,
        is_available=True
    ).exclude(id=product.id)[:4]

    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'product_detail.html', context)


def cart_view(request):
    """Xarid savati sahifasi"""
    context = {
        'cart_items': [],
        'subtotal': 0.00,
        'shipping_cost': 0,
        'total': 0.00,
    }
    return render(request, 'cart.html', context)


def checkout_view(request):
    """Buyurtmani rasmiylashtirish sahifasi"""
    context = {
        'cart_items': [],
        'subtotal': 0.00,
        'shipping_cost': 0,
        'total': 0.00,
    }
    return render(request, 'checkout.html', context)


def order_success_view(request):
    """Buyurtma tasdig'i sahifasi"""
    return render(request, 'order_success.html')


def login_view(request):
    """Tizimga kirish sahifasi"""
    return render(request, 'login.html')


def register_view(request):
    """Ro'yxatdan o'tish sahifasi"""
    return render(request, 'register.html')


def profile_view(request):
    """Foydalanuvchi profili sahifasi"""
    context = {
        'orders': [],
        'wishlist_count': 0,
    }
    return render(request, 'profile.html', context)


def wishlist_view(request):
    """Sevimlilar ro'yxati sahifasi"""
    context = {
        'wishlist_items': [],
    }
    return render(request, 'wishlist.html', context)


def about_view(request):
    """Biz haqimizda sahifasi"""
    return render(request, 'about.html')


def contact_view(request):
    """Aloqa va yordam sahifasi"""
    return render(request, 'contact.html')


def not_found_view(request):
    """404 xatolik sahifasi"""
    return render(request, '404.html')