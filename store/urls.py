# Django core imports
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Local app imports
from . import views
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ItemSearchListView,
    DeliveryListView,
    DeliveryDetailView,
    DeliveryCreateView,
    DeliveryUpdateView,
    DeliveryDeleteView,
    get_items_ajax_view,
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView
)

# URL patterns
urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Product URLs
    path(
        'products/',
        ProductListView.as_view(),
        name='productslist'
    ),
    path(
        'product/<slug:slug>/',
        ProductDetailView.as_view(),
        name='product-detail'
    ),
    path(
        'new-product/',
        ProductCreateView.as_view(),
        name='product-create'
    ),
path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),              # ✅
path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),         # ✅
path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),         # ✅

    
    # Item search
    path(
        'search/',
        ItemSearchListView.as_view(),
        name='item_search_list_view'
    ),
    
    # Delivery URLs
   # Delivery URLs
path(
    'deliveries/',
    DeliveryListView.as_view(),
    name='deliveries'
),
path(
    'delivery/<int:pk>/',
    DeliveryDetailView.as_view(),
    name='delivery-detail'
),
path(
    'delivery/<int:pk>/update/',
    DeliveryUpdateView.as_view(),
    name='delivery-update'
),
path(
    'delivery/<int:pk>/delete/',
    DeliveryDeleteView.as_view(),
    name='delivery-delete'
),

    
    # AJAX view
    path(
        'get-items/',
        get_items_ajax_view,
        name='get_items'
    ),
    
    # Category URLs
    path(
        'categories/',
        CategoryListView.as_view(),
        name='category-list'
    ),
    path(
        'categories/<slug:slug>/',
        CategoryDetailView.as_view(),
        name='category-detail'
    ),
    path(
        'categories/create/',
        CategoryCreateView.as_view(),
        name='category-create'
    ),
    path(
        'categories/<slug:slug>/update/',
        CategoryUpdateView.as_view(),
        name='category-update'
    ),
    path(
        'categories/<slug:slug>/delete/',
        CategoryDeleteView.as_view(),
        name='category-delete'
    ),
]

# Static media files configuration for development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )