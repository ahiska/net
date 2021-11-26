from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from .models import Article, Category
from hitcount.views import HitCountDetailView
from taggit.models import Tag

from .forms import CommentForm

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect


class ArticleListView(ListView):
    model = Article
    paginate_by = 10
    queryset = Article.objects.filter(status=True)

    # template_name = 'blog/article_list.html' #<app>/<model>_<viewtype>.html
    # ordering = ['-created'] # Model'de Article'ın sıralaması zaten tarihe göre ayarlı olduğunda buna burada gerek yok yada farklı bir unsura göre sıralama olabilir
    # context_object_name = 'article_list' # Varsayılan olarak object_list ve modelAdı_list yani zaten article_list 'dir.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_list'] = Article.objects.filter(status=True, featured=True).order_by('?')[0:3]
        # context['latest_list'] = get_list_or_404(Article, status=True) # En son yayınlara göre sıralamak için
        context['latest_list'] = Article.objects.filter(status=True).order_by(
            "-hit_count_generic__hits")[0:3]  # En çok okunana göre sıralamak için
        return context


class ArticleDetailView(HitCountDetailView):
    model = Article
    count_hit = True

    # context_object_name = 'article' # default <model>
    # template_name = 'blog/article_detail.html' # default <app>/<model>_<viewtype>.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['similar_articles'] = self.object.tags.similar_objects()
        context['featured_list'] = Article.objects.filter(status=True, featured=True).order_by('?')[0:3]
        context['latest_list'] = get_list_or_404(Article, status=True)[0:3]
        return context


class UserArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter(status=True)
    template_name = 'blog/user_articles.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'user_articles'
    paginate_by = 10

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return super(UserArticleListView, self).get_queryset().filter(author=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(username__iexact=self.kwargs.get('username'))
        context['featured_list'] = Article.objects.filter(status=True, featured=True).order_by('?')[0:3]
        context['latest_list'] = Article.objects.filter(status=True)[0:3]
        return context


class CategoryArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter(status=True)
    template_name = 'blog/category_posts.html'
    context_object_name = 'category_posts'
    paginate_by = 10

    # slug_field = 'slug'

    # def get_queryset(self):
    #     category = get_object_or_404(Category, slug=self.kwargs['slug'])
    #     return super(CategoryArticleListView, self).get_queryset().filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug__iexact=self.kwargs.get('slug'))
        context['featured_list'] = Article.objects.filter(status=True, featured=True).order_by('?')[0:3]
        context['latest_list'] = Article.objects.filter(status=True)[0:3]
        return context


class TagsListView(ListView):
    model = Tag
    template_name = 'blog/tags_list.html'
    context_object_name = 'tags_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_list'] = Article.objects.filter(status=True, featured=True).order_by('?')[0:3]
        context['latest_list'] = Article.objects.filter(status=True)[0:3]
        return context


class TagListView(ListView):
    model = Article
    template_name = 'blog/tag_list.html'
    context_object_name = 'tag_list'
    paginate_by = 10

    def get_queryset(self):
        tags = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return super().get_queryset().filter(tags=tags)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = Tag.objects.get(slug__iexact=self.kwargs.get('slug'))
        context['featured_list'] = Article.objects.filter(status=True, featured=True).order_by('?')[0:3]
        context['latest_list'] = Article.objects.filter(status=True)[0:3]
        return context


class AddCommentView(SuccessMessageMixin, CreateView):
    form_class = CommentForm
    success_url = reverse_lazy('article_detail')
    template_name = 'blog/article_detail.html'
    success_message = "Yorumunuz başarıyla gönderildi.!"

    def form_invalid(self, form):
        messages.error(self.request, 'Gönderiminizle ilgili bir sorun oluştu. Lütfen tekrar deneyin.')
        return HttpResponseRedirect('article_detail')

# def post_detail(request, pk, slug):
#     template_name = 'blog/article_detail.html'
#     post = get_object_or_404(Article, pk=pk, slug=slug)
#     comments = post.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     return render(request, template_name, {'post': post,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})