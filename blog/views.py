from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from .forms import BlogCreateForm

import logging
logger = logging.getLogger(__name__)

class BlogIndexView(generic.TemplateView):
    template_name = "blog_index.html"

class BlogListView(LoginRequiredMixin, generic.ListView):
    """ 日記一覧表示 """

    model = Blog
    template_name = 'blog_list.html'
    paginate_by = 2

    def get_queryset(self):
        blogs = Blog.objects.filter(user=self.request.user).order_by('-created_at')
        return blogs

class BlogDetailView(generic.TemplateView):
    template_name = "blog_detail.html"

class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    """ 日記作成表示 """

    model = Blog
    template_name = 'blog_create.html'
    form_class = BlogCreateForm
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.user = self.request.user
        blog.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)

class BlogUpdateView(generic.TemplateView):
    template_name = "blog_update.html"

class BlogDeleteView(generic.TemplateView):
    template_name = "blog_delete.html"