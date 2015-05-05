from django.contrib import admin
from .models import user, lastSession, accuracy

admin.site.register(user)
admin.site.register(lastSession)
admin.site.register(accuracy)
