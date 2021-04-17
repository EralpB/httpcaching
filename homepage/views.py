import time
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class Homepage(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        time.sleep(1)
        return super().dispatch(request, *args, **kwargs)


class DynamicHomepage(TemplateView):
    template_name = 'dynamicIndex.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        time.sleep(0.5)  # static content calculation
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        time.sleep(0.5)  # user profile calculations
        if request.user.is_authenticated:
            return JsonResponse({'authenticated': True, 'username': 'Eralp'})
        else:
            return JsonResponse({'authenticated': False})
