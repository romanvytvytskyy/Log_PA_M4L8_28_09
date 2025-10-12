from django.urls import path
from . import views

urlpatterns = [
    path('', views.PollListView.as_view(), name='poll-list'),
    path('<int:pk>/', views.PollDetailView.as_view(), name='poll-detail'),
    path('<int:pk>/results/', views.PollResultsView.as_view(), name='poll-result'),
    path('<int:pk>/vote/', views.vote, name='poll-vote'),
    path('<int:pk>/edit/', views.PollUpdateView.as_view(), name='poll-update'),
    path('<int:pk>/delete/', views.PollDeleteView.as_view(), name='poll-delete'),
    path('new/', views.PollCreateView.as_view(), name='poll-create'),
]
