from django.views import generic

class TestappView(generic.TemplateView): 
    template_name = "test.html"