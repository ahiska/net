from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from .models import Article, Category
from taggit.models import Tag


class ContextMixin(object):
    model = None
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_list'] = get_list_or_404(Article, status=True)
        context['featured_list'] = get_list_or_404(Article, status=True, featured=True)
        context['latest_list'] = get_list_or_404(Article, status=True)
        context['similar_articles'] = self.object.tags.similar_objects()
        context['user'] = get_object_or_404(User, username__iexact=self.kwargs.get('username'))
        context['category'] = get_object_or_404(Category, slug__iexact=self.kwargs.get('slug'))
        context['tag'] = get_object_or_404(Tag, slug__iexact=self.kwargs.get('slug'))
        return context


