from django.db import models as _models
from django.contrib.auth.models import User as _User


class Account(_models.Model):
    user = _models.ForeignKey(_User, verbose_name="user", on_delete=_models.CASCADE)