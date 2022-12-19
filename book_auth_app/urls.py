from django.urls import path
from .views import bookListCreateView,bookDetailView
urlpatterns = [
    path('',bookListCreateView.as_view(),name='book_list_create'),
    path('<int:pk>',bookDetailView.as_view(),name='book_detail'),

    
]