from django.db import models

# Create your models here.


class LastModifyModel(models.Model):

    last_modify = models.CharField(max_length=30)
    identifier = models.SmallIntegerField(default=1)

    def __str__(self) -> str:
        return self.last_modify
