"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from api.views import MenuItemsView, InventoryViewSet, StaffViewSet, OrderView, ItemOptionView, HighlightListView, HeaderConfigView, FooterConfigView, MainPageConfigView, LocationView, RestaurantListView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'inventory', InventoryViewSet)
router.register(r'staff', StaffViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/menu-items/<int:restaurant_id>/', MenuItemsView.as_view(), name='menu-items'),
    path('api/highlights/<int:restaurant_id>/', HighlightListView.as_view(), name='highlight-list'),
    path('api/header-config/<int:restaurant_id>/', HeaderConfigView.as_view(), name='header-config'),
    path('api/footer-config/<int:restaurant_id>/', FooterConfigView.as_view(), name='footer-config'),
    path('api/main-page-config/<int:restaurant_id>/', MainPageConfigView.as_view(), name='main-page-config'),
    path('api/restaurants/', RestaurantListView.as_view(), name='restaurant_list'),
    path('api/item-options/<int:restaurant_id>/', ItemOptionView.as_view(), name='itemoption-list'),
    path('api/locations/<int:restaurant_id>/', LocationView.as_view(), name='locations'),
    path('api/orders/<int:id>/', OrderView.as_view(), name='orders'),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)