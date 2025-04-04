from django.db import models


class TimeStampMixin(models.Model):
    """
    Mixin to add created and updated timestamps to a model.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
