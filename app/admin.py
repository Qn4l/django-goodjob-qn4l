from django.contrib import admin

from app.models import JobPost, Location, Author, Skill


class JobPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'salary', 'date_posted']
    ordering = ['-date_posted']
    list_filter = ['date_posted', 'salary']
    search_fields = ['title', 'salary', 'date_posted']
    search_help_text = "Search by job, salary or date posted"
    # fields = (('title', 'salary'), 'description')
    fieldsets = (
        ('Job Details', {'fields': ('title', 'description')}),
        ('More information', {
            'classes': ('collapse', 'autocomplete'),
            'fields': ('salary', 'expiry_date', 'slug')}),
    )


# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skill)
