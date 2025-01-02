import os

environment = os.getenv("DJANGO_ENV", "development")

if environment == "production":
    from .production import urlpatterns
else:
    from .development import urlpatterns