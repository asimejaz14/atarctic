from django.urls import path

from product import views
urlpatterns = [
    path('', views.ProductView.as_view(), name="Product View"),
    # path('dashboard', views.DashboardView.as_view(), name="Dashboard View"),
    path('<int:product_id>', views.ProductView.as_view(), name="Product View"),
    path('file/<int:image_id>', views.FileView.as_view(), name="File View"),
    path('video/<int:product_id>', views.VideoView.as_view(), name="Video View"),
    path('index', views.IndexView.as_view(), name="Index View"),

]

