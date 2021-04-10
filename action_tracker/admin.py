from django.contrib import admin

from .models import *


@admin.register(ActionType)
class ActionTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ActionStatus)
class ActionStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ActionEffect)
class ActionEffectAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('searcher', 'company', 'position', 'type', 'date',
                    'response_time', 'status', 'effect', 'comment', 'conclusions')

