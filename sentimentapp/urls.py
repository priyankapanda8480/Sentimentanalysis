from django.urls import path
from .views import predict_sentiment
from sentimentapp import views
# from django.contrib.auth.views import LoginView


urlpatterns = [
    # path('predict/', views.predict_sentiment, name='predict_sentiment'),
    path('index/', views.predict_sentiment, name='index'),
    # path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    






]
