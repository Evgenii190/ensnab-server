from django.contrib import admin

from .models import Service, ServiceContent, ServiceSlider, –°ooperation
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class ServiceContentFormAdmin(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = ServiceContent
        fields = '__all__'

class CoopForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = –°ooperation
        fields = '__all__'

class ServiceContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    list_display_links = ('id', 'title')
    form = ServiceContentFormAdmin

class CoopFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    list_display_links = ('id',)
    form = CoopForm

class ServicesSliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Service, ServiceAdmin)
admin.site.register(–°ooperation, CoopFormAdmin)
admin.site.register(ServiceContent, ServiceContentAdmin)
admin.site.register(ServiceSlider, ServicesSliderAdmin)