from django.conf import settings
import os

SCSS_EXECUTABLE = getattr(settings, "SCSS_EXECUTABLE", "sass")
SCSS_USE_CACHE = getattr(settings, "SCSS_USE_CACHE", True)
SCSS_CACHE_TIMEOUT = getattr(settings, "SCSS_CACHE_TIMEOUT", 60 * 60 * 24 * 30) # 30 days
SCSS_MTIME_DELAY = getattr(settings, "SCSS_MTIME_DELAY", 10) # 10 seconds

SCSS_INPUT_DIR = getattr(settings, "SCSS_INPUT_DIR", os.path.join(settings.STATIC_ROOT, 'scss'))
SCSS_OUTPUT_DIR = getattr(settings, "SCSS_OUTPUT_DIR", os.path.join(settings.MEDIA_ROOT, 'SCSS_CACHE'))
SCSS_OUTPUT_URL = getattr(settings, "SCSS_OUTPUT_URL", "/static/SCSS_CACHE")

SCSS_DEVMODE = getattr(settings, "SCSS_DEVMODE", False)
SCSS_DEVMODE_WATCH_DIRS = getattr(settings, "SCSS_DEVMODE_WATCH_DIRS", [settings.STATIC_ROOT])
SCSS_DEVMODE_EXCLUDE = getattr(settings, "SCSS_DEVMODE_EXCLUDE", ())
