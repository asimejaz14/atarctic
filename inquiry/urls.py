from django.urls import path

from inquiry import views
urlpatterns = [
    path('', views.InquiryView.as_view(), name="Inquiry View"),
    path('<int:inquiry_id>', views.InquiryView.as_view(), name="Inquiry View"),

]

