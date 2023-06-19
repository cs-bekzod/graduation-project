from django import forms
from django.contrib import admin
from apps.ishbor.models import Categories,Jobs,Candidates,Universities,Events,Contact


class JobsAdmin(admin.ModelAdmin):
    list_display = ('title','locations','job_type','phone','email','category','created_at')
    search_fields = ['title']
    
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title','locations','price','count','start_time','phone')
    search_fields = ['title']

class UniversitiesAdmin(admin.ModelAdmin):
    list_display = ('name','location','number_of_students','university_type', 'link')
    search_fields = ['name']
        
class CandidatesAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','locations','profession','experience','degree','job_type','status','email','created_at')
    search_fields = ['first_name', 'last_name']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','icon_name')
    search_fields = ['title']
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','title','email','created_at')
    search_fields = ['name','title']


admin.site.register(Jobs, JobsAdmin)
admin.site.register(Categories,CategoryAdmin)
admin.site.register(Candidates, CandidatesAdmin)
admin.site.register(Universities, UniversitiesAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(Contact,ContactAdmin)