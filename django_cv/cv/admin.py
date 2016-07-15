from django.contrib import admin
from .models import *


class PersonAdmin(admin.ModelAdmin):
    # fields = ['name', 'lastname', 'phone', 'mail', 'skype']
    list_display = ['name', 'lastname', 'phone', 'mail', 'skype', 'image_tag']
    readonly_fields = ['image_tag',]

    # only one Person in DB
    def has_add_permission(self, request):
        count = Person.objects.count()
        if count == 0:
            return True
        return False


admin.site.register(Person, PersonAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'fromtime', 'totime']

admin.site.register(Experience, ExperienceAdmin)


class KeySkillsAdmin(admin.ModelAdmin):
    list_display = ['skill']

admin.site.register(KeySkills, KeySkillsAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'faculty', 'fromtime', 'totime']

admin.site.register(Education, EducationAdmin)