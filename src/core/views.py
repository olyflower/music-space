from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "../templates/index.html"
    http_method_names = ["get"]
    extra_context = {"site_name": "Music-space"}
