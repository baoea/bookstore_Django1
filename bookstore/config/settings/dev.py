from .base import *  # NOQA

DEBUG = True

INSTALLED_APPS += (  # NOQA
    "debug_toolbar",
    "django_extensions",
)

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",
]

INTERNAL_IPS = ["127.0.0.1"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # NOQA
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] += (  # NOQA
    "rest_framework.renderers.BrowsableAPIRenderer",
)


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

