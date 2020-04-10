"""Fur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views as users_views
from blog import views as blog_views
from django.contrib.auth import views as auth_views
from searches import views as search_views
from django.conf import settings
from multiple import views as multiple_views
#cart
from django.urls import re_path
from django.conf.urls import url 
from orders import views as order_view
from carts import views as cart_view 
from cart import views as carte_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',users_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('about/', users_views.About,name='fur-home'),
    path('profile/',users_views.profile,name='profile'),
    path('blog-new/',blog_views.blog_post_create_view,name='blog-new'),
    path('blog/',include('blog.urls')),
    path('search/',search_views.Search_View,name='search'),
    path('front/',blog_views.FrontPage,name='FrontPage'),

    #cart Urls
    path('cart/',cart_view.View,name='cart'),
    #url('cart/(?P<id>[\d+]+)/$',cart_view.remove_from_cart,name='remove_cart'),
    #url('cart/(?P<slug>[\w-]+)/$',cart_view.update_cart,name='update_cart'),
    path('checkout/',order_view.checkout,name='checkout'),
    path('orders/',order_view.Orders,name='Orders'),
    #path('order/',cart_view.OrderSummary,name='order_summary')


    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', carte_view.add_to_cart, name="add_to_cart"),
    path("order-summary/", carte_view.order_details, name="order_summary"),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', carte_view.delete_from_cart, name='delete_item'),


]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# url('cart/(?P<slug>[\w-]+)/$',cart_view.update_cart,name='update_cart')