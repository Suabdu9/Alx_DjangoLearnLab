from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books

urlpatterns = [
    # Function-based view for listing books
    path('books/', views.list_books, name='list_books'),

    # Class-based view for library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Use LogoutView and specify the template for logout
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # User registration view (custom view)
    path('register/', views.register, name='register'),

    # Home page for logged-in users
    path('home/', views.home, name='home'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
