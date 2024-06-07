from django.urls import path
from . import views

urlpatterns = [
    path('personal_info/', views.personal_info, name='personal_info'),
    path('hobbies/', views.hobbies, name='hobbies'),

    path('Books_list/', views.Book_List_view),
    path('Books_list/<int:id>/', views.Book_Detail_view),

    path('current_time/', views.current_time, name='current_time'),
    path('random_numbers/', views.random_numbers, name='random_numbers'),
]
