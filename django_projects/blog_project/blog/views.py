from django.http import Http404
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "blogHome.html"
    context_object_name = "posts"

class BlogDetailView (DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return self.render_to_response({'error_message': 'No such post!'})

class AboutView(TemplateView):
    template_name = 'about.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = '__all__'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')