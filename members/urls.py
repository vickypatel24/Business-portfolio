from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('login/', views.login_view, name='login'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('change_password/', views.change_password, name='change_password'),
    path('home_page/', views.home_page, name='home_page'),
    path('log_out/', views.log_out, name='log_out'),
    path('master/', views.master, name='master'),
    path('product_list/', views.product_list, name='product_list'),
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('verify_otp/<int:user_id>/', views.verify_otp, name='verify_otp'),
    path('reset_password/<int:user_id>/', views.reset_password, name='reset_password'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)