from django.urls import path
from . import views

urlpatterns = [
    path('personal_info/', views.personal_info, name='personal_info'),
    path('hobbies/', views.hobbies, name='hobbies'),

    path('all_books/', views.all_books),
    path('teen/', views.books_tags_view),

    path('Books_list/', views.as_view(), name='Books_list'),
    path('Books_list/<int:id>/', views.BooksDetailView),

    path('Books_list/<int:id>/delete/', views.DeleteBooksView),
    path('Books_list/<int:id>/update/', views.EditBooksView),
    path('create_books/', views.CreateBooksView),
    path('search/', views.SearchView.as_view(), name='search'),

    path('current_time/', views.current_time, name='current_time'),
    path('random_numbers/', views.random_numbers, name='random_numbers'),
]
