from django.urls import path
from .views import *


urlpatterns = [
    path('', TovaryListView.as_view(), name='tovary'),
    path('create/', TovaryCreateView.as_view(), name='create'),
    path('update/<int:pk>', TovaryUpdateView.as_view(), name = 'update' ),
    path('detail/<int:pk>', TovaryDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', TovaryDeleteView.as_view(), name = 'delete'),
]