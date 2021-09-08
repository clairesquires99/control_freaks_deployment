from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class StoriesView(ListView):
    model = Post
    template_name = 'stories/stories.html'


class StoryView(DetailView):
    model = Post
    template_name = 'stories/story.html'
