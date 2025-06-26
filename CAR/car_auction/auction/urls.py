# # your_app/urls.py
# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views  # Your views.py file

# urlpatterns = [
#     path('', views.home, name='home'),  # Home page

#     path('add-car/', views.add_car, name='add_car'),  # Add car page

#     # Auth URLs - login/logout/signup
#     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
#     path('signup/', views.signup, name='signup'),

#     # Static content pages
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
#     path('terms/', views.terms, name='terms'),
#     path('car/<int:car_id>/', views.car_detail, name='car_detail'),
#         path('api/cars/', views.CarListAPIView.as_view(), name='car_list_api'),
#     path('api/cars/<int:pk>/', views.CarDetailAPIView.as_view(), name='car_detail_api'),
#     path('api/cars/<int:car_id>/bid/', views.PlaceBidAPIView.as_view(), name='car_bid_api'),
# ]
     

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('add-car/', views.add_car, name='add_car'),

    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
   path('logout/',views.user_logout,name='logout' ),
    path('signup/', views.signup, name='signup'),
   
    # Static pages
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),

    # Car detail with id
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),

    # API endpoints
    path('api/cars/', views.CarListAPIView.as_view(), name='car_list_api'),
    path('api/cars/<int:pk>/', views.CarDetailAPIView.as_view(), name='car_detail_api'),
    path('api/cars/<int:car_id>/bid/', views.PlaceBidAPIView.as_view(), name='car_bid_api'),
]
