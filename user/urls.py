from django.urls import path, include
from .views import RegisterView, LoginView, SocialLoginSuccess



urlpatterns = [
    # Your custom endpoints
    path("api/v1/register/", RegisterView.as_view(), name="register"),
    path("api/v1/login/", LoginView.as_view(), name="login"),

    # dj-rest-auth endpoints
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),

    # allauth endpoints
    path("api/v1/auth/", include("allauth.urls")),
    path("api/v1/auth/social/", include("allauth.socialaccount.urls")),

    # Social login success view
    path("api/v1/auth/social/login/success/", SocialLoginSuccess.as_view(), name="social"),


    #  for password reset
     path('api/v1/auth/', include('django.contrib.auth.urls')),

]


