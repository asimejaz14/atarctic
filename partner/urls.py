from django.urls import path

from partner import views
urlpatterns = [
    path('', views.PartnerView.as_view(), name="Partner View"),
    # path('dashboard', views.DashboardView.as_view(), name="Dashboard View"),
    path('<int:partner_id>', views.PartnerView.as_view(), name="Partner View"),
    path('file/<int:image_id>', views.FileView.as_view(), name="File View"),
    # path('index', views.IndexView.as_view(), name="Index View"),

]

