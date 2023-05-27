from unicodedata import name
from django.contrib import admin

# Register your models here.
from django.contrib import admin
# from . import models
from .models import (
    Category, 
        SubCategory,
        Title,
        Gender,  
        Region,

    Person, 
    Staff, 
        Profession,
        Rank,
        Department,
    Section,
    BoardOfDirector,
    Management, 
        Position,
        Department,
        Service,
        Office,
    Project,
        ProjectDetail,
        ProjectLead,
        ProjectMedia,
        ProjectOverview,
        ProjectTag  
)
""" Imports End"""

""" Categories Admin Start """
class SubCategoryInline(admin.StackedInline):
    model = SubCategory
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline,]
    list_display = ['name','description']
    extra = 0
    list_per_page = 5
    readonly_fields = ['slug',]
    search_fields = ['name','description']
    ordering = ['name',]
    # raw_id_fields = ['']

""" Categories Admin End """

""" Project Administration Start """
# Project Inlines
class ProjectOverviewInline(admin.TabularInline):
    model = ProjectOverview
    extra = 0

class ProjectDetailInline(admin.TabularInline):
    model = ProjectDetail

class ProjectLeadInline(admin.StackedInline):
    model = ProjectLead
    extra = 0
    list_display = ['staff']

class ProjectTagInline(admin.TabularInline):
    model = ProjectTag

class ProjectMediaInline(admin.TabularInline):
    model = ProjectMedia

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','description']

# Project Admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectOverviewInline,
        ProjectDetailInline,
        ProjectLeadInline,
        ProjectTagInline,
        ProjectMediaInline

        ]
    list_display = ['name','description']
    extra = 0
    search_fields = ['name','description']
    ordering = ['name',]
    list_per_page = 5
""" Project Administration End """

""" Section Start """
# Section Inlines
class DepartmentInline(admin.StackedInline):
    model = Department
    extra = 0
# Section Admin
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    inlines = [
        DepartmentInline,
        ]
    list_display = ['name',]
    extra = 0
    search_fields = ['name','description']
    ordering = ['name',]
    list_per_page = 5
""" Section End """

admin.site.register(Title)
admin.site.register(Gender)
admin.site.register(Region)
admin.site.register(Profession)
admin.site.register(Person)

# admin.site.register(BoardOfDirector)
# admin.site.register(Management)
# admin.site.register(Position)

admin.site.register(Staff)
admin.site.register(Rank)
admin.site.register(Office)
# admin.site.register(Service)
