from django.contrib import admin
from .models import RealEstate, Categories
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class RealestateAdminForm(forms.ModelForm):
    #description = forms.CharField(widget=CKEditorUploadingWidget())
    pass
    class Meta:
        model = RealEstate
        fields = '__all__'


class RealEstateAdmin(admin.ModelAdmin):
    form = RealestateAdminForm
    list_display = ('id', 'description', 'created_at', 'photo')
    list_display_links = ['id']
    search_fields = ('category',)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ['title']
    search_fields = ('categories',)


admin.site.register(RealEstate, RealEstateAdmin)

admin.site.register(Categories, CategoriesAdmin)

