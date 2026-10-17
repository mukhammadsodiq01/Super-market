from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from store import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home_view, name='home'),
    
    path('products/', views.products_view, name='product_list'),
    path('i18n/', include('django.conf.urls.i18n')),  # oxiriga vergul qo'yishni unutmang
    path('products/<slug:slug>/', views.product_detail_view, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-success/', views.order_success_view, name='order_success'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('404/', views.not_found_view, name='404'),

    path('subscribe/', views.home_view, name='subscribe_newsletter'),
    path('terms/', views.about_view, name='terms'),
    path('privacy/', views.about_view, name='privacy'),
    path('logout/', views.login_view, name='logout'),
    path('password-reset/', views.login_view, name='password_reset'),
    path('update-profile/', views.profile_view, name='update_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)