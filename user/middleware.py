from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone


class UserActiveMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.user.is_authenticated:
            request.user.last_active_datetime = timezone.now()
            request.user.save(update_fields=['last_active_datetime'])

    def process_response(self, request, response):
        if request.user.is_authenticated:
            request.session.set_expiry(60)
        return response
