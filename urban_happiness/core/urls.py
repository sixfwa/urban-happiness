from django.contrib import admin
from django.urls import path as _path, include as _include

urlpatterns = [
    _path("admin/", admin.site.urls),
    _path("", _include("pages.urls")),
    # _path("<str:username>/", _include("productivity.urls")),
]
