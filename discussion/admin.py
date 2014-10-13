from django.contrib import admin
from discussion.models import Discussion, Comment, Category


admin.site.register(Discussion)
admin.site.register(Comment)
admin.site.register(Category)
