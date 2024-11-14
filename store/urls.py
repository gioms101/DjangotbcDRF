from django.urls import path
from .views import ListPage, SendEmailPage, ProductDetailPage

app_name = 'store'

urlpatterns = [
    path('', ListPage.as_view(), name='main_page'),
    path('product/<slug:slug>', ProductDetailPage.as_view(), name='shop_detail_product'),
    path('category/<slug:slug>', ListPage.as_view(), name='specific_category'),
    path('contact/', SendEmailPage.as_view(), name='contact_page'),

]

