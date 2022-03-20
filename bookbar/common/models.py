from django.db import models
from django.utils import timezone

from bookbar.common.managers import SoftDeletionManager

'''
https://adriennedomingus.com/blog/soft-deletion-in-django
'''


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()
