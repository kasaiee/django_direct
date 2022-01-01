## Install

in `settings.py`

- add `django_direct` to the most top of `INSTALLED_APPS`

```
INSTALLED_APPS  = [
    'kartable',
    ...
    'django.contrib.admin',
]

```

- put `'django_direct.context_processors.get_app_list'` in the context processors


```
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'django_direct.context_processors.get_app_list'
            ],
        },
    },
]

```

- edit the admin url

```
from django.contrib import admin
from django.urls import path
from django_direct.direct_admin import site as admin_site

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', admin_site.urls),
]
```

- run `python manage.py collectstatic`

## How to use

- edit the  `__init__.py` of apps

```
default_app_config = '<APP_NAME>.apps.<APP_NAME>Config
```

- edit `apps.py` of apps

```
from django.apps import AppConfig

class <_APP_NAME>Config(AppConfig):
    order = 1  # priority of the app in the django_direct sidebar
    name = '<NAME OF THE APP>'
    verbose_name = '<PERSIAN NAME OF THE APP>'
    icon = '<ICON CSS CLASS NAME>'  # please use this icons https://themify.me/themify-icons
```

- edit `admin.py`. use `direct_admin` instead of `admin`

```
# from django.contrib import admin
from django_direct import direct_admin
from .models import YourModel


direct_admin.site.register(YourModel)
```