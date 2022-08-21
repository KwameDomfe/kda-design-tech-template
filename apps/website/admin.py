from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models

admin.site.register(models.SubCategories)
admin.site.register(models.Categories)

admin.site.register(models.Project)
admin.site.register(models.ProjectDetail)
admin.site.register(models.ProjectLead)
admin.site.register(models.ProjectMedia)
admin.site.register(models.ProjectOverview)
admin.site.register(models.ProjectTag)

admin.site.register(models.Title)
admin.site.register(models.Person)
admin.site.register(models.Gender)
admin.site.register(models.MaritalStatus)

admin.site.register(models.BoardOfDirectors)
admin.site.register(models.Management)

admin.site.register(models.Position)
admin.site.register(models.Profession)
admin.site.register(models.Rank)
admin.site.register(models.Department)
admin.site.register(models.Staff)

admin.site.register(models.Region)
admin.site.register(models.TownCity)
admin.site.register(models.Office)

