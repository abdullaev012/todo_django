from django.contrib import admin
from main.models import *

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'sent_at')

class DeleteAdmin(admin.ModelAdmin):
    list_display = ('deleted_title', 'deleted_description', 'deleted_sent_at')

class ElectedAdmin(admin.ModelAdmin):
    list_display = ('elected_title', 'elected_description', 'elected_sent_at')

admin.site.register(Todo, TodoAdmin)
admin.site.register(Delete, DeleteAdmin)
admin.site.register(Elected, ElectedAdmin)