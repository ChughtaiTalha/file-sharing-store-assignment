from django.db import models

from filestore.models import Folder
from filestore.models.base_model import BaseModel


class Status(models.TextChoices):
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'


class File(BaseModel):
    name = models.CharField(max_length=150, unique=True)
    status = models.CharField(choices=Status.choices, default=Status.PENDING)
    file_content = models.ForeignKey("Content", on_delete=models.CASCADE, null=True, blank=True)
    file_folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
