from django.contrib import admin
from .models import *


class PersonAdmin(admin.ModelAdmin):
    fields = ['name', 'lastname', 'phone', 'mail', 'skype']


admin.site.register(Person, PersonAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Experience, ExperienceAdmin)

# Register your models here.

# admin.site.register(KeySkills)
# admin.site.register(Education)