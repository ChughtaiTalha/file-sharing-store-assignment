import uuid

from django.db import models

from filestore.models import BaseModel


class Content(BaseModel):
    content = models.TextField()

