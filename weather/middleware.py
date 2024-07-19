from django.template.response import TemplateResponse
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse


class LastVisitedMiddleware(MiddlewareMixin):
    def process_template_response(self, request, response):
        if 'last_visited_pages' not in request.session:
            request.session['last_visited_pages'] = []

        last_visited_pages = request.session['last_visited_pages']

        current_path = request.path
        page_title = response.context_data.get('title', 'No Title')
        if current_path != reverse("weather:index"):
            last_visited_pages.append({'path': current_path, 'title': page_title})

        if len(last_visited_pages) > 5:
            last_visited_pages.pop(0)

        request.session['last_visited_page'] = last_visited_pages

        return response

