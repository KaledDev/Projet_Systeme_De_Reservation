"""
URL configuration for projet_reservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from restaurantHotelEvent import views
from utilisateurs import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/', admin.site.urls),
    path('inscription/', user_views.register, name='inscription'),
    path('', user_views.register, name='inscription'),
    path('login/', user_views.login_view, name='login'),
    path('home/', user_views.home, name='home'),
    path('logout/', user_views.logout_view, name='logout'),
    path('add_restaurant/', views.add_restaurant, name='add_restaurant'),
    path('add_hotel/', views.add_hotel, name='add_hotel'),
    path('add_event/', views.add_event, name='add_event'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('hotel/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/update/<int:event_id>/', views.update_event, name='update_event'),
    path('event/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('hotel/update/<int:id>/', views.update_hotel, name='update_hotel'),
    path('hotel/delete/<int:hotel_id>/', views.delete_hotel, name='delete_hotel'),
    path('restaurant/update/<int:id>/', views.update_restaurant, name='update_restaurant'),
    path('restaurant/delete/<int:id>/', views.delete_restaurant, name='delete_restaurant'),
    path('discover_restaurants/', user_views.discover_restaurants, name='discover_restaurants'),
    path('discover_hotels/', user_views.discover_hotels, name='discover_hotels'),
    path('discover_events/', user_views.discover_events, name='discover_events'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)