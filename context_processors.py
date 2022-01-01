from .direct_admin import site
from django.urls import reverse


def get_app_list(request):  # we have comment out it in footer
    if request.path.startswith(reverse('admin:index')):
        return {'APP_LIST': site.get_app_list(request)}
    else:  # none admin pages
        return {'APP_LIST': []}
