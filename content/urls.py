from django.urls import path
from content.views import * 
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page='login'),name="logout"),

    path('', BlogList,name = "index"),
    path('<pk>/', BlogDetailView,name = "blog-detail"),
    path('<pk>/update', BlogUpdateView.as_view(),name = "blog-update"),
    path('<pk>/delete/', BlogDeleteView.as_view(),name = "blog-delete"),
]

LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'login'