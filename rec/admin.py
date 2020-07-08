from django.contrib import admin
from rec import models

# Register your models here.

admin.site.index_title = "Recruitment"

admin.site.register(models.Notifications)
