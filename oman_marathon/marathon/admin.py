# from django.contrib import admin
# from .models import Run, Runner, RunRegistration

# @admin.register(Run)
# class RunAdmin(admin.ModelAdmin):
#     list_display = ('name', 'date')
#     search_fields = ('name', 'date')

# @admin.register(Runner)
# class RunnerAdmin(admin.ModelAdmin):
#     list_display = ('user', )
#     search_fields = ('user__username', 'user__email')  # Searching by user's username or email

# @admin.register(RunRegistration)
# class RunRegistrationAdmin(admin.ModelAdmin):
#     list_display = ('runner', 'run', 'registration_date')
#     search_fields = ('runner__user__username', 'run__name')  # Searching by runner's username or run name


from django.contrib import admin
from .models import Runner, ContactUsMessage

admin.site.register(Runner)
admin.site.register(ContactUsMessage)
