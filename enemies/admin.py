from django.contrib import admin

from .models import Enemy

class EnemyAdmin(admin.ModelAdmin):
    list_display = ('name', 'reason', 'revenge_taken',)

# Register your models here.
admin.site.register(Enemy, EnemyAdmin)