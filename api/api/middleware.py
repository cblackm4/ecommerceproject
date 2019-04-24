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

class UserIdCookieMiddleware(object):
    """
    Puts the id of the current authenticated user in the cookies.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated and not request.COOKIES.get('user'):
            response.set_cookie('user', request.user.id)
        elif not request.user.is_authenticated and request.COOKIES.get('user'):
            response.delete_cookie('user')
        return response