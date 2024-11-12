# from django.contrib.auth.views import LoginView
from django.urls import path
from .views import ListPage, RegisterPage, SendEmailPage, ProductDetailPage  #ContactView, CategoryPage, LogoutUser
# from user.forms import CustomAuthenticationForm

app_name = 'store'

urlpatterns = [
    path('', ListPage.as_view(), name='main_page'),
    path('product/<slug:slug>', ProductDetailPage.as_view(), name='shop_detail_product'),
    path('category/<slug:slug>', ListPage.as_view(), name='specific_category'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('contact/', SendEmailPage.as_view(), name='contact_page'),
    # path('login/', LoginView.as_view(template_name='login.html', form_class=CustomAuthenticationForm), name='login'),
    # path('logout/', LogoutUser.as_view(), name='logout'),
]

# path('order/checkout', views.checkout_page, name='checkout_page'),
# path('product/', views.shop_detail, name='shop_detail'),

