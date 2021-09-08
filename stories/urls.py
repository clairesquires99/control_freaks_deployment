from django.urls import path
from .views import StoriesView, StoryView

urlpatterns = [
    path('stories', StoriesView.as_view(), name='stories'),
    path('story/<int:pk>', StoryView.as_view(), name='story'),
]
