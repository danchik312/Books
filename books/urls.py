from django.urls import path
from . import views

urlpatterns = [
    path('personal_info/', views.personal_info, name='personal_info'),
    path('hobbies/', views.hobbies, name='hobbies'),

    path('all_books/', views.all_books),
    path('teen/', views.books_tags_view),

    path('Books_list/', views.Book_List_view),
    path('Books_list/<int:id>/', views.Book_Detail_view),

    path('employees/<int:id>/delete/', views.drop_books_view),
    path('employees/<int:id>/update/', views.edit_books_view),
    path('create_employee/', views.create_books_view),

    path('current_time/', views.current_time, name='current_time'),
    path('random_numbers/', views.random_numbers, name='random_numbers'),
]
