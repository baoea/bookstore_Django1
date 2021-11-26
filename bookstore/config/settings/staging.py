from .base import *  # NOQA

DEBUG = False

CORS_ORIGIN_WHITELIST = [

]

DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_BUCKET_NAME = ""
