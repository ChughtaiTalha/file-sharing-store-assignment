from django.urls import path
from user.views.user_views import UserLoginView, UserSignupView, UserDetailView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('details/', UserDetailView.as_view(), name='user-details'),
]
