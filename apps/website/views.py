import numbers
from django.shortcuts import render
from django.http import HttpResponse
from .models import (
    # Projects 
    Categories, SubCategories,
    Project, 
        ProjectOverview, 
        ProjectLead, 
        ProjectDetail, 
        ProjectTag, 
        ProjectMedia,
    # People
    Person, 
        Title,
        Gender, 
        MaritalStatus,
        Profession,

    Staff, 
        Rank,  
        Department,  
   

    # Practice
        # Board of Directors
        BoardOfDirectors, 
        # Management
        Management, Position,

    # Principles
        # Civic
    
        # Professionalism
    
        # Excellence
    
        # Integrity and Honesty
    
        # Timeliness and Cost Effectiveness
    
        # Sustainability
    
        # Empowerment
)    

import random


# Create your views here.
""" Tests Start """
def test(request):
    nameVar = 'Kuku' #String
    numberVar = random.randint(10, 123456) #pseudo random
    # From Database

    return HttpResponse('Hellow World')
""" Tests End """

""" Home Page start """
def index(request):
   
    ## pageNav querysets
    # Departments
    departments = Department.objects.all()

    # Ranks
    ranks = Rank.objects.all()

    # Staffs
    staff = Staff.objects.all()

    # Ranks
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]

    # Projects
    projectCategories = Categories.objects.all()

    print(departments)

    #pageNav querysets
    context = {
        'ranks' :ranks,
        'staff' :staff,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
        'departments' : departments,
        'project_categories_list' :projectCategories,
    } 

    return render(request,'website/index.html', context)

""" Home Page end """

""" News start """
def news(request):

    projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
        'project_categories_list':projectCategories_qs,
    } 
    return render(request,'website/news/news-home.html', context)
""" News End """

""" People start """
def people(request):
    #pageNav querysets
    rank = Rank.objects.all()
    staff = Staff.objects.all()
    departments = Department.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]
    projectCategories = Categories.objects.all()

    # print(rank)

    #pageNav querysets
    context = {
        'ranks' :rank,
        'staff' :staff,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
        'departments' :departments,       
        'project_categories_list' :projectCategories,
    } 
    # Render Template
    return render(request,'website/people/people-home.html', context)

def ranks(request, slug):
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]
    projectCategories_qs = Categories.objects.all()

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
        'project_categories_list' :projectCategories_qs,
    }
    return render(request,'website/people/principal-consultants/principal-consultants.html', context)
    
def principalConsultants(request):
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]
    projectCategories_qs = Categories.objects.all()

    #pageNav querysets
    context = {
        'ranks':rank,
        'senior_ranks':senior_ranks,
        'junior_ranks_1':junior_ranks_1,
        'junior_ranks_2':junior_ranks_2,
        'alumni_ranks':alumni_ranks,
        'project_categories_list':projectCategories_qs,
    }
    return render(request,'website/people/principal-consultants/principal-consultants.html', context)
    
def principalConsultantsDetails(request, id=None):
    persons = Person.objects.all()
    positions = Position.objects.all()
    depts = Department.objects.all()
    staff = Staff.objects.all()
    # ranks = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:6]
    junior_ranks = Rank.objects.all()[5:10]
    projectCategories_qs = Categories.objects.all()
    context = {
        'staff' : staff,
        'depts' : depts,
        'positions' : positions,
        # 'ranks' : ranks,
        'senior_ranks' : senior_ranks,
        'junior_ranks' : junior_ranks,
        'persons' : persons,
        'project_categories_list' :projectCategories_qs,
    } 
    return render(request,'website/people/principal-consultants/principal-consultant-details.html', context)

def seniorConsultants(request):
    
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]
    projectCategories_qs = Categories.objects.all()

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
        'project_categories_list' :projectCategories_qs,
    }

    return render(request,'website/people/senior-consultants/senior-consultants.html', context)

def seniorConsultantDetails(request):
    persons = Person.objects.all() #queryset
    positions = Position.objects.all()#queryset 
    persons = Person.objects.all()#queryset
    depts = Department.objects.all()#queryset
    staff = Staff.objects.all()#queryset 
    senior_ranks = Rank.objects.all()[0:6]#queryset
    junior_ranks = Rank.objects.all()[5:10]#queryset
    projectCategories_qs = Categories.objects.all()
    
    context = {
        'staff' : staff,
        'depts' : depts,
        'positions' : positions,
        'senior_ranks' : senior_ranks,
        'junior_ranks' : junior_ranks,
        'persons' : persons,
        'project_categories_list' :projectCategories_qs,
    } 
    return render(request,'website/people/senior-consultants/senior-consultant-details.html', context)

def consultants(request):
    
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]
    projectCategories_qs = Categories.objects.all()

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
        'project_categories_list' :projectCategories_qs,
    }

    return render(request,'website/people/consultants/consultants.html', context)

def consultantDetails(request):
  
    persons = Person.objects.all() #queryset
    positions = Position.objects.all()#queryset 
    persons = Person.objects.all()#queryset
    depts = Department.objects.all()#queryset
    staff = Staff.objects.all()#queryset 
    senior_ranks = Rank.objects.all()[0:6]#queryset
    junior_ranks = Rank.objects.all()[5:10]#queryset
    projectCategories_qs = Categories.objects.all()
    
    context = {
     
        'staff' : staff,
        'depts' : depts,
        'positions' : positions,
        'senior_ranks' : senior_ranks,
        'junior_ranks' : junior_ranks,
        'persons' : persons,
        'project_categories_list' :projectCategories,
    } 
    return render(request,'website/people/consultants/consultant-details.html', context)

def seniorProfessionals(request):
  
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]
    projectCategories_qs = Categories.objects.all()


    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
        'project_categories_list' :projectCategories_qs,
    }
    
    return render(request,'website/people/senior-professionals/senior-professionals.html', context)

def seniorProfessionalDetails(request):
    persons = Person.objects.all() #queryset
    positions = Position.objects.all()#queryset 
    persons = Person.objects.all()#queryset
    depts = Department.objects.all()#queryset
    staff = Staff.objects.all()#queryset 
    senior_ranks = Rank.objects.all()[0:6]#queryset
    junior_ranks = Rank.objects.all()[5:10]#queryset
    projectCategories_qs = Categories.objects.all()
    
    context = {
        'staff' : staff,
        'depts' : depts,
        'positions' : positions,
        'senior_ranks' : senior_ranks,
        'junior_ranks' : junior_ranks,
        'persons' : persons,
        'project_categories_list' :projectCategories_qs,
    } 
    return render(request,'website/people/senior-professionals/senior-professional-details.html', context)

def professionals(request):
    
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]
    projectCategories_qs = Categories.objects.all()

    print(rank)

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks, 
        'project_categories_list':projectCategories_qs,
    }
    return render(request,'website/people/professionals/professionals.html', context)

def assistantProfessionals(request):
    
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]
    projectCategories = Categories.objects.all()


    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
        'project_categories_list' :projectCategories,
    }

    return render(request,'website/people/assistant-professionals.html', context)

def probationers(request):
    
   #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]
    projectCategories = Categories.objects.all()

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
        'project_categories_list' :projectCategories,
    }

    return render(request,'website/people/probationers.html', context)

def nationalServicePersonnel(request):
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]
    projectCategories = Categories.objects.all()

    print(rank)

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
        'project_categories_list' :projectCategories,

    }

    return render(request,'website/people/service-personnel.html', context)

def supportingTeam(request):
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]
    projectCategories = Categories.objects.all()


    print(rank)

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
        'project_categories_list' :projectCategories,
    }
    return render(request,'website/people/supporting-team.html', context)
""" People End """

""" Practice start """
# Practice Home
def practice(request):

    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }

    return render(request,'website/practice/practice-home.html', context)

# Practice History
def history(request):
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }
    return render(request, 'website/practice/history.html', context)

# Practice Mandate
def mandate(request):
    
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }
    return render(request, 'website/practice/mandate.html', context)

# Practice Functions
def functions(request):
    
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }
    return render(request, 'website/practice/functions.html', context)

# Practice Mission, Vision, and Values
def missionVisionAndValues(request):
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }
    return render(request, 'website/practice/mission-vision-and-values.html', context)

# Practice Sector Ministry
def sectorMinistry(request):
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }
    return render(request, 'website/practice/sector-ministry.html', context)

# Practice Corporate_Governance
def corporateGovernance(request):
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }

    return render(request, 'website/practice/corporate_governance/board-of-directors-home.html', context)

# Practice Board Chairman
def boardChairman(request):
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }

    return render(request, 'website/practice/corporate_governance/board_of_directors_home.html', context)

# Practice Board Member
def boardMember(request):
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }

    return render(request, 'website/practice/corporate-governance/board-of-directors-home.html', context)

# Practice Management
def management(request):
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }
    return render(request, 'website/practice/management/management-home.html', context)

# Practice Manging Director Details
def managingDirectorDetails(request):
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }
    return render(request, 'website\practice\management\managing-director.html', context)

# Practice Deputy Manging Director Details
def deputyManagingDirectorDetails(request):
    ranks = Rank.objects.all()
    projects_qs = Project.objects.all()
    projectCategories_qs = Categories.objects.all()

    context = {
            'projects_list': projects_qs,
            'project_categories_list':projectCategories_qs,
            'ranks':ranks
        }
    return render(request, 'website\practice\management\deputy-managing-director.html', context)

# Practice Head of Department Details
def headsOfDepartmentsDetails(request):
    ranks = Rank.objects.all()
    projects_qs = Project.objects.all()
    projectCategories_qs = Categories.objects.all()

    context = {
            'projects_list': projects_qs,
            'project_categories_list':projectCategories_qs,
            'ranks':ranks
        }
    return render(request, 'website\practice\management\head-of-department-details.html', context)

# Practice Regional Consultant Details
def regionalConsultantDetails(request):
    ranks = Rank.objects.all()
    projects_qs = Project.objects.all()
    projectCategories_qs = Categories.objects.all()

    context = {
            'projects_list': projects_qs,
            'project_categories_list':projectCategories_qs,
            'ranks':ranks
        }
    return render(request, 'website\practice\management\regional-consultant-details.html', context)

# Practice Corporate Responsibilities
def corporateResponsibilities(request):

    projectCategories_qs = Categories.objects.all()

    context = {
        'project_categories_list':projectCategories_qs,
    }
    return render(request, 'website/practice/corporate_responsibilities.html', context)

# Practice Alliances
def alliances(request):

    projectCategories_qs = Categories.objects.all()

    context = {
        'project_categories_list':projectCategories_qs,
    }

    return render(request, 'website/practice/alliances.html', context)

# Practice Client Speak
def clientSpeak(request):

    projectCategories_qs = Categories.objects.all()


    context = {
        'project_categories_list':projectCategories_qs,

    }
    return render(request, 'website/practice/client_speak.html', context)

""" Practice End """

""" Principles start """
def principles(request):

    # persons = Person.objects.all() #queryset
    # positions = Position.objects.all()#queryset 
    # depts = Department.objects.all()#queryset
    # staff = Staff.objects.all()#queryset  print(staff)
   
    # senior_ranks = Rank.objects.all()[0:5]#queryset
    # junior_ranks = Rank.objects.all()[5:10]#queryset

    projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        'project_categories_list':projectCategories_qs,
        # 'project_categories_list_1':projectCategories_qs_1,
        # 'project_categories_list_2':projectCategories_qs_2
    } 

    return render(request,'website/principles/principles-home.html', context)
    
def civic(request):
    # persons = Person.objects.all() #queryset
    # positions = Position.objects.all()#queryset 
    # depts = Department.objects.all()#queryset
    # staff = Staff.objects.all()#queryset  print(staff)
   
    # senior_ranks = Rank.objects.all()[0:5]#queryset
    # junior_ranks = Rank.objects.all()[5:10]#queryset

    projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        'project_categories_list':projectCategories_qs,
        # 'project_categories_list_1':projectCategories_qs_1,
        # 'project_categories_list_2':projectCategories_qs_2
    } 

    
    return render(request,'website/principles/civic.html', context)

def professionalism(request):

    # persons = Person.objects.all() #queryset
    # positions = Position.objects.all()#queryset 
    # depts = Department.objects.all()#queryset
    # staff = Staff.objects.all()#queryset  print(staff)
   
    # senior_ranks = Rank.objects.all()[0:5]#queryset
    # junior_ranks = Rank.objects.all()[5:10]#queryset

    projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        'project_categories_list':projectCategories_qs,
        # 'project_categories_list_1':projectCategories_qs_1,
        # 'project_categories_list_2':projectCategories_qs_2
    } 

    return render(request,'website/principles/professionalism.html', context)

def excellence(request):

    # persons = Person.objects.all() #queryset
    # positions = Position.objects.all()#queryset 
    # depts = Department.objects.all()#queryset
    # staff = Staff.objects.all()#queryset  print(staff)
   
    # senior_ranks = Rank.objects.all()[0:5]#queryset
    # junior_ranks = Rank.objects.all()[5:10]#queryset

    projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        'project_categories_list':projectCategories_qs,
        # 'project_categories_list_1':projectCategories_qs_1,
        # 'project_categories_list_2':projectCategories_qs_2
    } 
    return render(request,'website/principles/excellence.html', context)

def integrityAndHonesty(request):

    # persons = Person.objects.all() #queryset
    # positions = Position.objects.all()#queryset 
    # depts = Department.objects.all()#queryset
    # staff = Staff.objects.all()#queryset  print(staff)
   
    # senior_ranks = Rank.objects.all()[0:5]#queryset
    # junior_ranks = Rank.objects.all()[5:10]#queryset

    projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        'project_categories_list':projectCategories_qs,
        # 'project_categories_list_1':projectCategories_qs_1,
        # 'project_categories_list_2':projectCategories_qs_2
    } 

    return render(request,'website/principles/integrity-and-honesty.html', context)

def timelinessAndCostEffectiveness(request):

    # persons = Person.objects.all() #queryset
    # positions = Position.objects.all()#queryset 
    # depts = Department.objects.all()#queryset
    # staff = Staff.objects.all()#queryset  print(staff)
   
    # senior_ranks = Rank.objects.all()[0:5]#queryset
    # junior_ranks = Rank.objects.all()[5:10]#queryset

    projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        'project_categories_list':projectCategories_qs,
        # 'project_categories_list_1':projectCategories_qs_1,
        # 'project_categories_list_2':projectCategories_qs_2
    } 

    return render(request,'website/principles/timeliness_and_cost_effectiveness.html', context)

def sustainability(request):

    # persons = Person.objects.all() #queryset
    # positions = Position.objects.all()#queryset 
    # depts = Department.objects.all()#queryset
    # staff = Staff.objects.all()#queryset  print(staff)
   
    # senior_ranks = Rank.objects.all()[0:5]#queryset
    # junior_ranks = Rank.objects.all()[5:10]#queryset

    projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        'project_categories_list':projectCategories_qs,
        # 'project_categories_list_1':projectCategories_qs_1,
        # 'project_categories_list_2':projectCategories_qs_2
    } 

    return render(request,'website/principles/sustainability.html', context)

def empowerment(request):

    # persons = Person.objects.all() #queryset
    # positions = Position.objects.all()#queryset 
    # depts = Department.objects.all()#queryset
    # staff = Staff.objects.all()#queryset  print(staff)
   
    # senior_ranks = Rank.objects.all()[0:5]#queryset
    # junior_ranks = Rank.objects.all()[5:10]#queryset

    projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        'project_categories_list':projectCategories_qs,
        # 'project_categories_list_1':projectCategories_qs_1,
        # 'project_categories_list_2':projectCategories_qs_2
    } 

    return render(request,'website/principles/empowerment.html', context)

""" Principles End """

""" projects start """
def projects(request):
    projects_qs = Project.objects.all()
    ranks = Rank.objects.all()
    projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    Sub_Categories_qs = SubCategories.objects.all()#print(projectCategories_qs)
    projectCategories_qs_1 = Categories.objects.all()[:5]
    projectCategories_qs_2 = Categories.objects.all()[5:]
    
    context = {
                'projects_list': projects_qs,
                'project_categories_list':projectCategories_qs,
                'project_sub_categories':Sub_Categories_qs,
                'project_categories_list_1':projectCategories_qs_1,
                'project_categories_list_2':projectCategories_qs_2,
                'ranks':ranks
            }
    
    return render(request,'website/projects/projects-home.html', context)

def projectsList(request):

    projects = Project.objects.all()
    projectCategories = Categories.objects.all()
    projectCategories_1 = Categories.objects.all()[:5]
    projectCategories_2 = Categories.objects.all()[5:]

    projectSubCategories = SubCategories.objects.all()
    
    
    context = {
                'projects_list': projects,
                'project_categories_list':projectCategories,
                'project_subcategory':projectSubCategories,
                'project_categories_list_1':projectCategories_1,
                'project_categories_list_2':projectCategories_2
            }

    return render(request, 'website/projects/projects_list_view.html', context)

def projectDetails(request, slug = None):
        
        projects = Project.objects.all()
        projectCategories = Categories.objects.all() 
        project_obj = None
        if slug is not None:
            project_obj = Project.objects.get(slug=slug)
            project_lead = ProjectLead.objects.all()
            project_qs = Project.objects.all()
            projectOverview = ProjectOverview.objects.all()
        
            context = {
                'project_categories_list':projectCategories,
                'projects_list': projects,
                'project' : project_obj,
                'project_lead':project_lead,
                'project_list':project_qs,
                'projectOverview' :projectOverview
        }
        
        return render(request, 'website/projects/projects_detail_view.html', context)

def projectsMap(request):
        
#         projects_qs = Project.objects.all() #print(projects_qs)
#         projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
#         projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
#         projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
        context = {
#                 'projects_list': projects_qs,
#                 'projectcategories_list':projectCategories_qs,
#                 'projectcategories_list_1':projectCategories_qs_1,
#                 'projectcategories_list_2':projectCategories_qs_2
                
            }

        return render(request, 'website/projects/projects_map_view.html', context)

def projectMap(request):
        
#         projects_qs = Project.objects.all() #print(projects_qs)
#         projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
#         projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
#         projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
        context = {
#                 'projects_list': projects_qs,
#                 'projectcategories_list':projectCategories_qs,
#                 'projectcategories_list_1':projectCategories_qs_1,
#                 'projectcategories_list_2':projectCategories_qs_2
                
            }

        return render(request, 'website/projects/projects_map_view.html', context)

def projectFilms(request):
        
#         projects_qs = Project.objects.all() #print(projects_qs)
#         projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
#         projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
#         projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
#                 'projects_list': projects_qs,
#                 'projectcategories_list':projectCategories_qs,
#                 'projectcategories_list_1':projectCategories_qs_1,
#                 'projectcategories_list_2':projectCategories_qs_2
                
    }
        
    return render(request, 'website/projects/projects_films_view.html', context)

def projectFilmDetails(request):
        
#         projects_qs = Project.objects.all() #print(projects_qs)
#         projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
#         projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
#         projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
#                 'projects_list': projects_qs,
#                 'projectcategories_list':projectCategories_qs,
#                 'projectcategories_list_1':projectCategories_qs_1,
#                 'projectcategories_list_2':projectCategories_qs_2
                
    }
        
    return render(request, 'website/projects/projects_films_view.html', context)

def projectCategories(request):
    
    projects_qs = Project.objects.all()#print(projects_qs)
    projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
            'projects_list': projects_qs,
            'project_categories_list':projectCategories_qs,
            'projectcategories_list_1':projectCategories_qs_1,
            'projectcategories_list_2':projectCategories_qs_2,
    }

    return render(request, 'website/projects/project_categories/project_categories_home_view.html', context)

def projectCategoriesList(request):
    
#     projectCategories = Categories.objects.all()
    
    context = {
#         'project-categories-list' : projectCategories
    }

    return render(request, 'website/projects/project_categories/project_categories_list_view.html', context)

def projectCategoryDetails(request, slug = None):
    
    projects_qs = Project.objects.all()
    projectCategories = Categories.objects.all()
    projectCategories_1 = Categories.objects.all()[:5]
    projectCategories_2 = Categories.objects.all()[5:]
        
    projectCategory = None
    if slug is not None:
        projectCategory = Categories.objects.get(slug=slug)

    context = {
            'Categories' : projectCategory,
            'projects_list': projects_qs,
            'project_categories_list':projectCategories,
            'project-categories_list_1':projectCategories_1,
            'project-categories_list_2':projectCategories_2         
    }

   

    return render(request, 'website/projects/project_categories/project_categories_detail_view.html', context)

def projectSubCategories(request):
        
#     project_families_queryset = None
#     if id is not None:
#         sub_categories_queryset = Sub_Categories.objects.all()
    

    context = {
#         'project_families_list': sub_categories_queryset     
}

    return render(request, 'website/projects/project_families_list_view.html', context)

def projectSubCategoriesDetails(request, id=None):
        
#     project_families_queryset = None
#     if id is not None:
#         project_families_queryset = Sub_Categories.objects.all()
    
    context = {
#         'project_families_list': project_families_queryset
    }

    return render(request, 'website/projects/project_families_list_view.html', context)
""" projectse end """

""" Publications Start """
def publications(request):

#     persons = Person.objects.all() #queryset
#     positions = Position.objects.all()#queryset 
#     depts = Department.objects.all()#queryset
#     staff = Staff.objects.all()#queryset  print(staff)
   
#     senior_ranks = Rank.objects.all()[0:5]#queryset
#     junior_ranks = Rank.objects.all()[5:10]#queryset

#     projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
#     projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
#     projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
#         'staff' : staff,
#         'depts' : depts,
#         'positions' : positions,
#         'senior_ranks' : senior_ranks,
#         'junior_ranks' : junior_ranks,
#         'persons' : persons,
#         'project_categories_list':projectCategories_qs,
#         'project_categories_list_1':projectCategories_qs_1,
#         'project_categories_list_2':projectCategories_qs_2
    } 

    return render(request,'website/publications/publications-home.html', context)
""" Publications End """

""" Search Start """
def search(request):

#     persons = Person.objects.all() #queryset
#     positions = Position.objects.all()#queryset 
#     depts = Department.objects.all()#queryset
#     staff = Staff.objects.all()#queryset  print(staff)
   
#     senior_ranks = Rank.objects.all()[0:5]#queryset
#     junior_ranks = Rank.objects.all()[5:10]#queryset

#     projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
#     projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
#     projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
     context = {
       
#         'staff' : staff,
#         'depts' : depts,
#         'positions' : positions,
#         'senior_ranks' : senior_ranks,
#         'junior_ranks' : junior_ranks,
#         'persons' : persons,
#         'project_categories_list':projectCategories_qs,
#         'project_categories_list_1':projectCategories_qs_1,
#         'project_categories_list_2':projectCategories_qs_2
    } 

     return render(request,'website/search/search-home.html', context)
""" Search End """

""" Misc. Start """
def _404Page(request):

    # tree = 'It is getiing interesting' 

    context = {
        # 'variable' : tree
    } 

    return render(request,'website/misc/404_page.html', context)

def blankPage(request):

    tree = 'It is getiing interesting' 

    context = {
        'variable' : tree
    } 

    return render(request,'website/misc/blank_page.html', context)

def blankTemplate(request):

    tree = 'It is getiing interesting' 

    context = {
        'variable' : tree
    } 

    return render(request,'website/misc/blank_template_page.html', context)

def policiesAndGuidelines(request):

    tree = 'It is getiing interesting' 

    context = {
        'variable' : tree
    } 

    return render(request,'website/misc/policies_and_guidelines.html', context)

def privacyStatement(request):

    tree = 'It is getiing interesting' 

    context = {
        'variable' : tree
    } 

    return render(request,'website/misc/privacy_statement.html', context)
""" Misc. End """