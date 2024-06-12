from django.utils import timezone
from django.http import HttpRequest, HttpResponseForbidden
from django.core.cache import cache

def set_useragent_on_request_miiddleware(get_response):

    print("initial call")

    def middleware(request: HttpRequest):
        print("before get response")
        request.user_agent = request.META.get("HTTP_USER_AGENT", 'unknown') # type: ignore
        response = get_response(request)
        print("after get response")
        return response

    return middleware

class CountRequestsMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        self.requests_count = 0
        self.response_count = 0
        self.exception_counts = 0

    def __call__(self, request: HttpRequest):
        self.requests_count +=1
        print('requests count', self.requests_count)
        response = self.get_response(request)
        self.response_count += 1
        print('resposes count', self.response_count)
        return response
    
    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exception_counts += 1
        print('got', self.exception_counts, 'exceptions so far')


class ThrottlingMiddleware:
    THROTTLE_DURATION = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        ip_address = self.get_user_ip(request)

        cache_key = f'throttle_{ip_address}'

        last_request_time = cache.get(cache_key)

        if last_request_time and (timezone.now() - last_request_time).seconds < self.THROTTLE_DURATION:
            return HttpResponseForbidden("Too many requests")
        
        cache.set(cache_key, timezone.now(), self.THROTTLE_DURATION)

        return self.get_response(request)
    
    def get_user_ip(self, request: HttpRequest):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    