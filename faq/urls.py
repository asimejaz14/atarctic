from django.urls import path
from .views import FAQView

urlpatterns = [
    path('', FAQView.as_view(), name='faq-list-create'),
    path('<int:faq_id>', FAQView.as_view(), name='faq-detail'),
]
