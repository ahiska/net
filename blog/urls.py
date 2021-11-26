from django.urls import path
from . import views
from .views import CategoryArticleListView, ArticleListView, ArticleDetailView, UserArticleListView, TagsListView, TagListView


urlpatterns = [
    #path('', article_list_view, name='blog'),
    path('', ArticleListView.as_view(), name='blog'),
    path('<int:pk>/<slug:slug>', ArticleDetailView.as_view(), name='article_detail'),
    path('yazar/<str:username>', UserArticleListView.as_view(), name='user_articles'),
    path('kategori/<slug:slug>', CategoryArticleListView.as_view(), name='list_by_category'),
    #path('kategori/<slug:slug>', category_posts, name='list_by_category'),
    path('etiket/', TagsListView.as_view(), name='tags_list_url'),
    path('etiket/<str:slug>', TagListView.as_view(), name='tag_detail_url'),
    # path('etiket/<str:slug>', tag_detail, name='tag_detail_url')
]