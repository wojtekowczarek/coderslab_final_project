from django.contrib import admin
from .models import (List, Item)


# Register your models here.
@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class TagAdmin(admin.ModelAdmin):
    pass
