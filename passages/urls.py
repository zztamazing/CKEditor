from django.urls import  path
from .views import editPassage, passages

urlpatterns = [
    path('', passages, name='passages'),
    path('edit/', editPassage, name='edit-passage'),
]


