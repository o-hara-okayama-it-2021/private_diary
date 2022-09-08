from django.views import generic

class BlogIndexView(generic.TemplateView):
    template_name = "blog_index.html"

class BlogListView(generic.TemplateView):
    template_name = "blog_list.html"

class BlogDetailView(generic.TemplateView):
    template_name = "blog_detail.html"

class BlogCreateView(generic.TemplateView):
    template_name = "blog_create.html"

class BlogUpdateView(generic.TemplateView):
    template_name = "blog_update.html"

class BlogDeleteView(generic.TemplateView):
    template_name = "blog_delete.html"