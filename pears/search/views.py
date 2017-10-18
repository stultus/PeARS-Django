import logging
from django.views.generic import TemplateView
from search.models import OpenVector
from search.utils import query_distribution

# Get an instance of a logger
logger = logging.getLogger(__name__)


class LandingView(TemplateView):
    template_name = 'apps/search/landing.html'

    def get(self, request, **kwargs):
        query = request.GET.get('q')
        context = self.get_context_data(**kwargs)
        if query:
            query_dist = query_distribution(query)

            context['q'] = query
        return self.render_to_response(context)
