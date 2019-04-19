"""
Custom middleware classes.
"""
from django.http import HttpResponseRedirect
from django.urls import reverse

class EnforceAuthMiddleware(object):
    """
    Requires the user to be logged in to access the site contents.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        if not request.user.is_authenticated:
            if (request.path == reverse('login')
                or request.path == reverse('signup')):
                return response
            else:
                return HttpResponseRedirect(reverse('login'))
        return response
