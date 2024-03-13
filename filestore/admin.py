# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Folder, File


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ("name", "parent_folder", "user")


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "file_content", "file_folder")
