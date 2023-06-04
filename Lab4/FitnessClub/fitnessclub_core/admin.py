from django.contrib import admin
from .models import GymMembership, Gym, Schedule

@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    list_filter = ['schedule', 'gym_membership']

@admin.register(GymMembership)
class GymMembershipAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'cost']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['open_time', 'close_time', 'is_works_on_weekends']
    fields = [('open_time', 'close_time'), 'is_works_on_weekends']

