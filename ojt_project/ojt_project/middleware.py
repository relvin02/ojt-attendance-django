from django.http import Http404
from django.shortcuts import render


class Friendly404Middleware:
    """Middleware to render a friendly 404 page for unresolved or missing pages.

    This catches Http404 exceptions and also converts responses with
    status_code==404 into a friendly template. It helps avoid exposing
    the Django debug URL listing when users manually change the path.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            if getattr(response, 'status_code', None) == 404:
                return render(request, 'attendance/404_friendly.html', status=404)
            return response
        except Http404:
            return render(request, 'attendance/404_friendly.html', status=404)
