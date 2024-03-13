from django.contrib.auth import get_user_model
from django.db import models

from filestore.models.base_model import BaseModel

User = get_user_model()


class Folder(BaseModel):
    name = models.CharField(max_length=150)
    parent_folder = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
