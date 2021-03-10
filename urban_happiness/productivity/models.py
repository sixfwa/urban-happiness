from django.db import models as _models
from accounts import models as _account_model


class Goal(_models.Model):
    """
    A goal represents a collective idea of something to achieve
    """

    account = _models.ForeignKey(
        _account_model.Account, verbose_name="account", on_delete=_models.CASCADE
    )
    goal = _models.CharField(verbose_name="goal title", max_length=255)
    target_date_completion = _models.DateField(
        verbose_name="target date completion", null=True, blank=True
    )
    date_completed = _models.DateTimeField(
        verbose_name="date completed", null=True, blank=True
    )
    is_complete = _models.BooleanField(verbose_name="is achieved", default=False)
    reason = _models.TextField(verbose_name="reason for goal")


class Task(_models.Model):
    account = _models.ForeignKey(
        _account_model.Account, verbose_name="account", on_delete=_models.CASCADE
    )
    associated_goal = _models.ForeignKey(
        Goal,
        verbose_name="associated goal",
        null=True,
        blank=True,
        on_delete=_models.SET_NULL,
    )
    task = _models.CharField(verbose_name="task title", max_length=255)
    is_complete = _models.BooleanField(verbose_name="is complete", default=False)
    reason = _models.TextField(verbose_name="reason for task")
    target_date = _models.DateField(verbose_name="target date")
    completion_date = _models.DateTimeField(verbose_name="completion date")
