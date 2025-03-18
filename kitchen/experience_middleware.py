import re
from django.shortcuts import redirect

class ExperienceMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:
            years_of_experience = getattr(request.user, 'years_of_experience', 0)
            request_path = request.path_info.lower()
            if years_of_experience < 5 and request_path == '/cooks/':
                return redirect('kitchen:index')

            restricted_urls = [
                '/cooks/delete/',
                '/ingredient/create/',
                '/dish/create/',
                '/dishtype/create/',
            ]

            if any(request_path.startswith(url) for url in restricted_urls):
                if years_of_experience < 2:
                    return self.redirect_if_not_enough_experience(years_of_experience)

            if re.match(r'^/dishtype/\d+/delete/', request_path) or \
               re.match(r'^/ingredient/\d+/delete/', request_path) or \
               re.match(r'^/dish/\d+/delete/', request_path) or \
               re.match(r'^/dishtype/\d+/update/', request_path) or \
               re.match(r'^/ingredient/\d+/update/', request_path) or \
               re.match(r'^/dish/\d+/update/', request_path) or \
               re.match(r'^/dish/\d+/toggle-assign/', request_path):
                if years_of_experience < 2:
                    return self.redirect_if_not_enough_experience(years_of_experience)

            if re.match(r'^/cooks/\d+/update/', request_path):
                user_id = int(request_path.split('/')[2])
                if user_id != request.user.id and years_of_experience < 10:
                    return self.redirect_if_not_enough_experience(years_of_experience)

            if re.match(r'^/cooks/\d+/delete/', request_path):
                if years_of_experience < 10:
                    return self.redirect_if_not_enough_experience(years_of_experience)

        return self.get_response(request)

    def redirect_if_not_enough_experience(self, years_of_experience):
        return redirect('kitchen:index')
