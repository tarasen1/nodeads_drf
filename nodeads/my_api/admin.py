from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Group, Element



class IsChildFilter(admin.SimpleListFilter):

    title = 'is child'

    parameter_name = 'is_child'

    default_value = None

    def lookups(self, request, model_admin):
        return (
        ('is_child', _('Is a child')),
        ('not_child', _('Not a child')),
                )
    def queryset(self, request, queryset):
        if self.value() == 'is_child':
            return queryset.filter(parent_group__isnull=False)
        if self.value() == 'not_child':
            return queryset.filter(parent_group__isnull=True)

class IsChekedFilter(admin.SimpleListFilter):

    title = 'is checked'

    parameter_name = 'is_checked'

    default_value = None

    def lookups(self, request, model_admin):
        return (
        ('is_checked', _('Is checked')),
        ('not_checked', _('Not checked')),
                )
    def queryset(self, request, queryset):
        if self.value() == 'is_checked':
            return queryset.filter(checked__isnull=False)
        if self.value() == 'not_checked':
            return queryset.filter(checked__isnull=True)

class GroupAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'name', 'dscr', 'parent_group', 'num_child_groups', 'num_child_elements')
    list_filter = (IsChildFilter,)

class ElementAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'name', 'checked', 'dscr', 'parent_group')
    list_filter = (IsChekedFilter,)

admin.site.register(Group, GroupAdmin)
admin.site.register(Element, ElementAdmin)

#
# from django.contrib import admin
# from adminfilters.models import Species, Breed
#

#
# @admin.register(Breed)
# class BreedAdmin(admin.ModelAdmin):
#     list_display = ('name', 'species', )
#     list_filter = (SpeciesListFilter, )
