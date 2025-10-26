from django.urls import path
from .views import *

urlpatterns = [
    path('', EventListView.as_view(), name = 'event-list'),
    path('new/', EventCreateView.as_view(), name = 'event-create'),
    path('<int:pk>/', EventDetailView.as_view(), name = 'event-detail'),
    path('<int:pk>/edit/', EventUpdateView.as_view(), name = 'event-update'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name = 'event-delete'),
]
