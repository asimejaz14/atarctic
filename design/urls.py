from django.urls import path

from design import views
urlpatterns = [
    path('banner', views.BannerView.as_view(), name="Banner View"),
    path('footer', views.FooterView.as_view(), name="Footer View"),
    path('about', views.AboutView.as_view(), name="About View"),
    path('mission', views.MissionView.as_view(), name="About View"),

]

