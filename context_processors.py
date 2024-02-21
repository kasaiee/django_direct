from django.conf import settings
from django.urls import reverse

from .direct_admin import site


def get_app_list(request):  # we have comment out it in footer
    if request.path.startswith(reverse("admin:index")):
        return {"APP_LIST": site.get_app_list(request)}
    else:  # none admin pages
        return {"APP_LIST": []}


def get_settings(request):
    if request.path.startswith(reverse("admin:index")):
        return {"settings": settings}
    else:  # none admin pages
        return {"settings": {}}
