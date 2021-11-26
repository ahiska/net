from blog.views import ArticleListView



# Kod tekrarı yapmamak için Blog uygulamasındaki ArticleListView buraya çektim
class HomePageListView(ArticleListView):
    template_name = 'home/index.html'