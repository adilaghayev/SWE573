from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, EntryCreateView, EntryDetailView, EntryListView, EntryUpdateView, EntryDeleteView
from user import views as user_views
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='community-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='community-about'),

    path('entry/<int:pk>', EntryDetailView.as_view(), name='entry-detail'),
    path('entry/new/', EntryCreateView.as_view(), name='entry-create'),
    path('entry/<int:pk>/update', EntryUpdateView.as_view(), name='entry-update'),
    path('entry/<int:pk>/delete', EntryDeleteView.as_view(), name='entry-delete'),
]

