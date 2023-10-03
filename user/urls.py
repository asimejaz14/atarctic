from django.urls import path
from .views import UserView, UserLoginView

urlpatterns = [
    path('', UserView.as_view(), name='create-user'),
    path('<int:user_id>', UserView.as_view(), name='update-delete-get-user'),
    path('login', UserLoginView.as_view(), name='login'),
]
