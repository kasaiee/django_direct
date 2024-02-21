from .direct_admin import site
from django.urls import reverse
from django.conf import settings


def get_app_list(request):  # we have comment out it in footer
    if request.path.startswith(reverse('admin:index')):
        user = request.user
        is_setad = user.groups.filter(name='setad') or getattr(user, 'is_setad', False)
        app_list = site.get_app_list(request)
        if is_setad:
            for i, app in enumerate(app_list):
                for j, model in enumerate(app['models']):
                    if model['object_name'] == 'Accommodation':
                        del app_list[i]['models'][j]
                    elif model['object_name'] == 'Image':
                        del app_list[i]
        return {'APP_LIST': app_list}
    else:  # none admin pages
        return {'APP_LIST': []}


def get_settings(request):
    if request.path.startswith(reverse('admin:index')):
        return {'settings': settings}
    else:  # none admin pages
        return {'settings': {}}
