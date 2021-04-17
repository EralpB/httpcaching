import time
from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        time.sleep(1)
        super().dispatch(request, *args, **kwargs)