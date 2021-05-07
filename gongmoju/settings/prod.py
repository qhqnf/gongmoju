from .common import *

DEBUG = os.environ.get("DEBUG") in ["True", "t", "TRUE", "1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ["DB_HOST"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "NAME": os.environ.get("DB_NAME", "postgres"),
        "PORT": "5432",
    }
}
