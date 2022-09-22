from django.urls import (path, include)
from . views import (
    index,
    people,
        ranks, 
        principalConsultants, 
        seniorConsultants,
        consultants, 
        seniorProfessionals,
        professionals,
        assistantProfessionals, 
        probationers,
        supportingTeam,
        nationalServicePersonnel, 

        principalConsultantsDetails,
        seniorConsultantDetails,
        consultantDetails,
        seniorProfessionalDetails,
        
       
    practice,
        history, 
        mandate, 
        functions,
        missionVisionAndValues,
        
        sectorMinistry, 
        corporateGovernance, 
        boardChairman,
        boardMember,

        management, 
        managingDirectorDetails,
        deputyManagingDirectorDetails, 
        headsOfDepartmentsDetails,
        regionalConsultantDetails, 
        alliances,
        clientSpeak, 
        corporateResponsibilities,

    principles, 
        professionalism,
        civic, 
        excellence,
        integrityAndHonesty, 
        timelinessAndCostEffectiveness, 
        sustainability, 
        empowerment, 

    projects,
        projectsList,
        projectsMap, 
        projectFilms, 
        projectDetails,
        projectCategories,
        projectCategoryDetails, 
        projectSubCategories, 
        projectSubCategories, 
    search,

    news,

    publications,
)

app_name = 'website'

urlpatterns = [
    # Home Page
    path('', index, name='index'),
    # People
    path('people/',include
        (
            [
                path('', people, name='people-home'),

                path('<slug:slug>/', 
                    ranks, 
                    name='ranks'),

                path('principal-consultants/', 
                    principalConsultants, 
                    name='principal-consultants'),

                path('principal-consultants/principal-consultant-details', 
                    principalConsultantsDetails, 
                    name='principal-consultant-details'),
                
                path('senior-consultants/', 
                    seniorConsultants, 
                    name='senior-consultants'),

                path('senior-consultants/senior-consultant-details', 
                    seniorConsultantDetails, 
                    name='senior-consultant-details'),
                
                path('consultants/', 
                    consultants, 
                    name='consultants'),
                    
                path('consultants/consultant-details', 
                    consultantDetails, 
                    name='consultant-details'),
                
                path('senior-professionals', 
                    seniorProfessionals, 
                    name='senior-professionals'),

                path('senior-professionals/senior-professional-details', 
                    seniorProfessionalDetails, 
                    name='senior-professional-details'),
                
                path('professionals', 
                    professionals, 
                    name='professionals'),

                path('assistant-professionals', 
                    assistantProfessionals, 
                    name='assistant-professionals'),

                path('probationers', 
                    probationers, 
                    name='probationers'),

                path('supporting-team', 
                    supportingTeam, 
                    name='supporting-team'),

                path('service-personnel', 
                    nationalServicePersonnel, 
                    name='national-service-personnels'),
            ]
        )
    ),
        
    # Practice
    path('practice/', include
        (
            [
                path('', 
                    practice, 
                    name = 'practice-home'),
                path('history', 
                    history, 
                    name = 'history'),
                path('mandate', 
                    mandate, 
                    name = 'mandate'),
                path('functions', 
                    functions, name  = 'functions'),    
                path('mission-vision-values', 
                    missionVisionAndValues, 
                    name = 'mission-vision-values'), 
                
                path('corporate-governance/', 
                    corporateGovernance, 
                    name = 'corporate-governance'),
                path('corporate-governance/board-chairman-details', 
                    boardChairman, 
                    name = 'corporate-governance-board-chairman'),
                path('corporate-governance/board-members/board-member-details', 
                    boardMember, 
                    name = 'corporate-governance-board-member'),
                
                path('management/', 
                    management, 
                    name = 'management'),
                    
                path('management/managing-director-details', 
                    managingDirectorDetails, 
                    name = 'managing-director'),

                path('management/deputy-managing-director-details', 
                    deputyManagingDirectorDetails, 
                    name = 'deputy-managing-director'),

                path('management/heads-of-departments/head-of-department-details', 
                    headsOfDepartmentsDetails, 
                    name = 'head-of-department-details'),

                path('management/regional-consultants/regional-consultant-details', 
                    regionalConsultantDetails, 
                    name = 'regional-consultant-consultant-details'),
                
                path('sector-ministry', 
                    sectorMinistry, 
                    name = 'sector-ministry'),

                path('alliances/', 
                    alliances, name ='alliances'),

                path('client-speak', 
                    clientSpeak, 
                    name = 'client-speak'),

                path('corporate-responsibilities', 
                    corporateResponsibilities, 
                    name = 'corporate-responsibilities'),
            ]
        )
    ),
    
    # Principles
    path('principles/', include([
            path('', 
                principles, 
                name = 'principles-home'),
            path('professionalism', 
                professionalism, 
                name = 'principles-professionalism'),
            path('civic', 
                civic, 
                name = 'principles-civic'),
            path('excellence', 
                excellence, 
                name = 'principles-excellence'),
            path('integrity-and-honesty', 
                integrityAndHonesty, 
                name = 'principles-integrity-and-honesty'),
            path('timeliness-and-cost-effectiveness', 
                timelinessAndCostEffectiveness, 
                name = 'principles-timeliness-and-cost-effectiveness'),
            path('sustainability', 
                sustainability, 
                name = 'principles-sustainability'),
            path('empowerment', 
                empowerment, 
                name = 'principles-empowerment'),])
    ),

    # Projects          
    path("projects/", include([
            path('', 
                projects, 
                name = 'projects-home'),

            path('projects-list/', 
                projectsList, 
                name='projects-list'),

            path('projects-map-home/', 
                projectsMap, 
                name='projects-maps-home'),

            path('projects-films-home/', 
                projectFilms, 
                name='project-films-home'),

            path('project-category/project-family/project-type/<slug:slug>/', 
                projectDetails, 
                name='project-details'),

            
            path('project-categories-home/', 
                projectCategories, 
                name='project-categories-home'),
            path('project-categories-list/', 
                projectCategories, 
                name='project-categories-list'),
            path('<slug:slug>/', 
                projectCategoryDetails, 
                name='project-category-details'),

            path('project-sub-categories-home/', 
                projectSubCategories, 
                name='project-sub-categories-home'),

            path('project-sub-categories-list/', 
                projectSubCategories, 
                name='project-sub-categories-list'),

            path('<slug:slug>/', 
                projectSubCategories, 
                name='project-sub-categories-details'),

            # path('project-types-home/', 
            #   project_Types_Home, 
            # name='project-types-home'),
            # path('project-types-list/', 
            #   project_Types_List, 
            # name='project-types-list'),
            # path('<slug:slug>/', 
            #   project_Type_Details, 
            # name='project-type-details'),
        ])
    ),
    
    # Search
    path('search/', 
        search, 
        name = 'search'),
    
    # News
    path('news/', 
        news, 
        name = 'news-home'),

    #Publications
    path('publications/', 
        publications, 
        name = 'publications-home'),
     ] 
    
