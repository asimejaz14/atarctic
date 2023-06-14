from django.urls import path

from partner import views
urlpatterns = [
    path('', views.PartnerView.as_view(), name="Partner View"),
    # path('dashboard', views.DashboardView.as_view(), name="Dashboard View"),
    path('<int:partner_id>', views.PartnerView.as_view(), name="Partner View"),
    # path('index', views.IndexView.as_view(), name="Index View"),

]

