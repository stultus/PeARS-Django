import logging
from django.views.generic import TemplateView

# Get an instance of a logger
logger = logging.getLogger(__name__)


class LandingView(TemplateView):
    template_name = 'apps/search/landing.html'

    def get(self, request, **kwargs):
        query = request.GET.get('q')
        context = self.get_context_data(**kwargs)
        if query:
            context['q'] = query
        return self.render_to_response(context)
