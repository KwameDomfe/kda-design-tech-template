from django.urls import (path, include)
from . import views

app_name = 'website'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # People
    path('people/',include
        (
            [
                path('', views.people, name='people-home'),

                path('<slug:slug>/', 
                    views.ranks, 
                    name='ranks'),

                path('principal-consultants/', 
                    views.principalConsultants, 
                    name='principal-consultants'),

                path('principal-consultants/principal-consultants-details', 
                    views.principalConsultantsDetails, 
                    name='principal-consultants-detail'),
                
                path('senior-consultants/', 
                    views.seniorConsultants, 
                    name='senior-consultants'),

                path('senior-consultants/senior-consultant-details', 
                    views.seniorConsultantDetails, 
                    name='senior-consultant-details'),
                
                path('consultants/', 
                    views.consultants, 
                    name='consultants'),
                    
                path('consultants/consultant-details', 
                    views.consultantDetails, 
                    name='consultant-details'),
                
                path('senior-professionals', 
                    views.seniorProfessionals, 
                    name='senior-professionals'),

                path('senior-professionals/senior-professional-details', 
                    views.seniorProfessionalDetails, 
                    name='senior-professional-details'),
                
                path('professionals', 
                    views.professionals, 
                    name='professionals'),

                path('assistant-professionals', 
                    views.assistantProfessionals, 
                    name='assistant-professionals'),

                path('probationers', 
                    views.probationers, 
                    name='probationers'),

                path('supporting-team', 
                    views.supportingTeam, 
                    name='supporting-team'),

                path('service-personnel', 
                    views.nationalServicePersonnel, 
                    name='national-service-personnels'),
            ]
        )
    ),
        
    # Practice
    path('practice/', include([
        path('', 
            views.practice, 
            name = 'practice-home'),
        path('alliances/', 
            views.alliances, name ='alliances'),
        path('client-speak', 
            views.clientSpeak, 
            name = 'client-speak'),
        path('corporate-governance/', 
            views.corporateGovernance, 
            name = 'corporate-governance'),
        path('corporate-governance/board-chairman', 
            views.corporateGovernance, 
            name = 'corporate-governance-board-chairman'),
        path('corporate-governance/board-members/', 
            views.corporateGovernance, 
            name = 'corporate-governance-board-member'),
        path('corporate-governance/board-members/board-member-details', 
            views.corporateGovernance, 
            name = 'corporate-governance-board-member'),
        path('corporate-responsibilities', 
            views.corporateResponsibilities, 
            name = 'corporate-responsibilities'),
        path('functions', 
            views.functions, name  = 'functions'),
        path('history', 
            views.history, 
            name = 'history'),
        path('mandate', 
            views.mandate, 
            name = 'mandate'),
        path('mission-vision-values', 
            views.missionVisionAndValues, 
            name = 'mission-vision-values'),
        path('sector-ministry', 
            views.sectorMinistry, 
            name = 'sector-ministry'),
        path('management/', 
            views.management, 
            name = 'management'),
        path('management/managing-director', 
            views.managingDirectorDetails, 
            name = 'managing-director'),
        path('management/deputy-managing-director-engineering', 
            views.deputyManagingDirectorDetails, 
            name = 'deputy-managing-director-engineering'),
        path('management/deputy-managing-director-architecture-and-planning', 
            views.deputyManagingDirectorDetails, 
            name = 'deputy-managing-director-architecture-planning'),
        path('management/departments/', 
            views.corporateGovernance, 
            name = 'heads-of-departments'),
        path('management/departments/heads-of-departments/', 
            views.headOfDepartmentDetails, 
            name = 'heads-of-departments'),
        path('management/departments/heads-of-departments/head-of-department-details', 
            views.corporateGovernance, 
            name = 'head-of-department-details'),
        path('management/regional-consultants', 
            views.corporateGovernance, 
            name = 'regional-consultants'),
        path('management/regional-consultants/regional-consultant-details', 
            views.corporateGovernance, 
            name = 'regional-consultant-consultant-details'),
        path('client-speak', 
            views.corporateGovernance, 
            name = 'client-speak'),
        path('offices/', 
            views.corporateGovernance, 
            name = 'offices'),])
    ),
    
    # Principles
    path('principles/', include([
            path('', 
                views.principles, 
                name = 'principles-home'),
            path('professionalism', 
                views.professionalism, 
                name = 'principles-professionalism'),
            path('civic', 
                views.civic, 
                name = 'principles-civic'),
            path('excellence', 
                views.excellence, 
                name = 'principles-excellence'),
            path('integrity-and-honesty', 
                views.integrityAndHonesty, 
                name = 'principles-integrity-and-honesty'),
            path('timeliness-and-cost-effectiveness', 
                views.timelinessAndCostEffectiveness, 
                name = 'principles-timeliness-and-cost-effectiveness'),
            path('sustainability', 
                views.sustainability, 
                name = 'principles-sustainability'),
            path('empowerment', 
                views.empowerment, 
                name = 'principles-empowerment'),])
    ),

    # Projects          
    path("projects/", include([
            path('', 
                views.projects, 
                name = 'projects-home'),

            path('projects-list/', 
                views.projectsList, 
                name='projects-list'),

            path('projects-map-home/', 
                views.projectsMap, 
                name='projects-maps-home'),

            path('projects-films-home/', 
                views.projectsFilms, 
                name='project-films-home'),

            path('project-category/project-family/project-type/<slug:slug>/', 
                views.projectDetails, 
                name='project-details'),

            path('project-categories-home/', 
                views.projectCategories, 
                name='project-categories-home'),

            path('project-categories-list/', 
                views.projectCategories, 
                name='project-categories-list'),

            path('<slug:slug>/', 
                views.projectCategoryDetails, 
                name='project-category-details'),

            path('project-families-home/', 
                views.projectSubCategories, 
                name='project-families-home'),

            path('project-families-list/', 
                views.projectSubCategories, 
                name='project-families-list'),

            # path('<slug:slug>/', 
            #     views.projectSubCategories, 
            #     name='project-family-details'),

            # path('project-types-home/', 
            #   views.project_Types_Home, 
            # name='project-types-home'),
            # path('project-types-list/', 
            #   views.project_Types_List, 
            # name='project-types-list'),
            # path('<slug:slug>/', 
            #   views.project_Type_Details, 
            # name='project-type-details'),
        ])
    ),
    
    # Search
    path('search/', 
        views.search, 
        name = 'search'),
    
    # News
    path('news/', 
        views.news, 
        name = 'news-home'),

    #Publications
    path('publications/', 
        views.publications, 
        name = 'publications-home'),
     ] 
    
