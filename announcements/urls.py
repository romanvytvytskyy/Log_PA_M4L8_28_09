from django.urls import path
from .views import *

urlpatterns = [
    path('', AnnouncementListView.as_view(), name = 'announcement-list'),
    path('new/', AnnouncementCreateView.as_view(), name = 'announcement-create'),
    path('<int:pk>/edit/', AnnouncementUpdateView.as_view(), name = 'announcement-update'),
    path('<int:pk>/delete/', AnnouncementDeleteView.as_view(), name = 'announcement-delete'),
]
