from django.shortcuts import render
from django.http import HttpResponse
from .models import (
    Categories, SubCategories,
    Project, ProjectOverview, ProjectLead, ProjectDetail, ProjectTag,ProjectMedia,
    Person,
    BoardOfDirectors, Management,
    Staff, Profession, Rank, Position, Office, Department,  
    TownCity, Region,
    Gender, Title,MaritalStatus,
)

# Create your views here.
""" Tests Start """
def test(request):
    return HttpResponse('Hellow World')
""" Tests End """

""" Home Page start """
def index(request):
   
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    # projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            # 'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }

    return render(request,'website/index.html', context)

""" Home Page end """

""" News start """
def news(request):

    context = {
            
    } 
    return render(request,'website/news/news-home.html', context)
""" News End """

""" People start """
def people(request):
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

    # Render Template
    return render(request,'website/people/people-home.html', context)

# def ranks(request):
#     #pageNav querysets
#     rank = Rank.objects.all()
#     senior_ranks = Rank.objects.all()[0:3]
#     junior_ranks_1 = Rank.objects.all()[3:7]
#     junior_ranks_2 = Rank.objects.all()[7:9]
#     alumni_ranks = Rank.objects.all()[9:]
#     projectCategories = Categories.objects.all()

#     print(rank)

#     #pageNav querysets
#     context = {
#         'ranks' :rank,
#         'senior_ranks' :senior_ranks,
#         'junior_ranks_1' :junior_ranks_1,
#         'junior_ranks_2' :junior_ranks_2,
#         'alumni_ranks' :alumni_ranks,
#         'project_categories_list' :projectCategories,
#     } 

#     # Render Template
#     return render(request,'website/people/people-home.html', context)

def principalConsultants(request):
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]

    print(rank)

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
    }
    return render(request,'website/people/principal-consultants/principal-consultants.html', context)

def principalConsultantsDetails(request):
    # persons = Person.objects.all() #queryset
    # positions = Position.objects.all()#queryset 
    # persons = Person.objects.all()#queryset
    # depts = Department.objects.all()#queryset
    # staff = Staff.objects.all()#queryset 
    # senior_ranks = Rank.objects.all()[0:6]#queryset
    # junior_ranks = Rank.objects.all()[5:10]#queryset
    
    context = {
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons
    } 
    return render(request,'website/people/principal-consultants/principal-consultant-details.html', context)

def seniorConsultants(request):
    
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]

    print(rank)

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
    }

    return render(request,'website/people/senior-consultants/senior-consultants.html', context)

def seniorConsultantDetails(request):
    # persons = Person.objects.all() #queryset
    # positions = Position.objects.all()#queryset 
    # persons = Person.objects.all()#queryset
    # depts = Department.objects.all()#queryset
    # staff = Staff.objects.all()#queryset 
    # senior_ranks = Rank.objects.all()[0:6]#queryset
    # junior_ranks = Rank.objects.all()[5:10]#queryset
    
    context = {
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons
    } 
    return render(request,'website/people/senior-consultants/senior-consultant-details.html', context)

def consultants(request):
    
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]

    print(rank)

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
    }

    return render(request,'website/people/consultants/consultants.html', context)

def consultantDetails(request):
  
    # persons = Person.objects.all() #queryset
    # positions = Position.objects.all()#queryset 
    # persons = Person.objects.all()#queryset
    # depts = Department.objects.all()#queryset
    # staff = Staff.objects.all()#queryset 
    # senior_ranks = Rank.objects.all()[0:6]#queryset
    # junior_ranks = Rank.objects.all()[5:10]#queryset
    
    context = {
     
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons
    } 
    return render(request,'website/people/consultants/consultant-details.html', context)

def seniorProfessionals(request):
  
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]

    print(rank)

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
    }
    
    return render(request,'website/people/senior-professionals/senior-professionals.html', context)

def seniorProfessionalDetails(request):
    # persons = Person.objects.all() #queryset
    # positions = Position.objects.all()#queryset 
    # persons = Person.objects.all()#queryset
    # depts = Department.objects.all()#queryset
    # staff = Staff.objects.all()#queryset 
    # senior_ranks = Rank.objects.all()[0:6]#queryset
    # junior_ranks = Rank.objects.all()[5:10]#queryset
    
    context = {
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons
    } 
    return render(request,'website/people/senior-professionals/senior-professional-details.html', context)

def professionals(request):
    
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]

    print(rank)

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
    }
    return render(request,'website/people/professionals/professionals.html', context)

def assistantProfessionals(request):
    
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]

    print(rank)

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
    }

    return render(request,'website/people/assistant-professionals.html', context)

def probationers(request):
    
   #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]

    print(rank)

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
    }

    return render(request,'website/people/probationers.html', context)

def nationalServicePersonnel(request):
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]

    print(rank)

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
    }

    return render(request,'website/people/service-personnel.html', context)

def supportingTeam(request):
    #pageNav querysets
    rank = Rank.objects.all()
    senior_ranks = Rank.objects.all()[0:3]
    junior_ranks_1 = Rank.objects.all()[3:7]
    junior_ranks_2 = Rank.objects.all()[7:9]
    alumni_ranks = Rank.objects.all()[9:]

    print(rank)

    #pageNav querysets
    context = {
        'ranks' :rank,
        'senior_ranks' :senior_ranks,
        'junior_ranks_1' :junior_ranks_1,
        'junior_ranks_2' :junior_ranks_2,
        'alumni_ranks' :alumni_ranks,
    }
    return render(request,'website/people/supporting-team.html', context)
""" People End """

""" Practice start """
# Practice Home
def practice(request):

    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    # projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            # 'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }

    return render(request,'website/practice/practice-home.html', context)

# Practice History
def history(request):
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    # projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            # 'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }
    return render(request, 'website/practice/history.html', context)

# Practice Mandate
def mandate(request):
    
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    # projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            # 'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }
    return render(request, 'website/practice/mandate.html', context)

# Practice Functions
def functions(request):
    
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    # projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            # 'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }
    return render(request, 'website/practice/functions.html', context)

# Practice Mission, Vision, and Values
def missionVisionAndValues(request):
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    # projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            # 'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }
    return render(request, 'website/practice/mission-vision-and-values.html', context)

# Practice Sector Ministry
def sectorMinistry(request):
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    # projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            # 'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }
    return render(request, 'website/practice/sector-ministry.html', context)

# Practice Corporate_Governance
def corporateGovernance(request):
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    # projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            # 'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }

    return render(request, 'website/practice/corporate_governance/board_of_directors_home.html', context)

# Practice Corporate_Governance
def management(request):
    # ranks = Rank.objects.all()
    # projects_qs = Project.objects.all()
    # projectCategories_qs = Categories.objects.all()

    context = {
            # 'projects_list': projects_qs,
            # 'project_categories_list':projectCategories_qs,
            # 'ranks':ranks
        }
    return render(request, 'website/practice/management/management-home.html', context)

# Practice Corporate Responsibilities
def corporateResponsibilities(request):
    context = {

    }
    return render(request, 'website/practice/corporate_responsibilities.html', context)

# Practice Alliances
def alliances(request):
    
    context = {

    }

    return render(request, 'website/practice/alliances.html', context)

# Practice Client Speak
def clientSpeak(request):
    context = {

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

    # projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        # 'project_categories_list':projectCategories_qs,
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

    # projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        # 'project_categories_list':projectCategories_qs,
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

    # projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        # 'project_categories_list':projectCategories_qs,
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

    # projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        # 'project_categories_list':projectCategories_qs,
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

    # projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        # 'project_categories_list':projectCategories_qs,
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

    # projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        # 'project_categories_list':projectCategories_qs,
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

    # projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        # 'project_categories_list':projectCategories_qs,
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

    # projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    context = {
       
        # 'staff' : staff,
        # 'depts' : depts,
        # 'positions' : positions,
        # 'senior_ranks' : senior_ranks,
        # 'junior_ranks' : junior_ranks,
        # 'persons' : persons,
        # 'project_categories_list':projectCategories_qs,
        # 'project_categories_list_1':projectCategories_qs_1,
        # 'project_categories_list_2':projectCategories_qs_2
    } 

    return render(request,'website/principles/empowerment.html', context)

""" Principles End """

""" projects start """
def projects(request):
    projects_qs = Project.objects.all()
    ranks = Rank.objects.all()
    Categories_qs = Categories.objects.all()#print(projectCategories_qs)
    Sub_Categories_qs = SubCategories.objects.all()#print(projectCategories_qs)
    projectCategories_qs_1 = Categories.objects.all()[:5]
    projectCategories_qs_2 = Categories.objects.all()[5:]
    
    print(projects_qs)
    print(Categories_qs)
    context = {
                'projects_list': projects_qs,
                'project_categories':Categories_qs,
                'project_sub_categories':Sub_Categories_qs,
                'project_categories_list_1':projectCategories_qs_1,
                'project_categories_list_2':projectCategories_qs_2,
                'ranks':ranks
            }
    
    return render(request,'website/projects/projects-home.html', context)

def projectsList(request):
    projects_qs = Project.objects.all()#print(projects_qs)
    Categories_qs = Categories.objects.all()#print(projectCategories_qs)
    Sub_Categories_qs = SubCategories.objects.all()#print(projectCategories_qs)
    projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)

    

    context = {
                'projects_list': projects_qs,
                'project_category':Categories_qs,
                'project_subcategory':Sub_Categories_qs,
                'project_categories_list_1':projectCategories_qs_1,
                'project_categories_list_2':projectCategories_qs_2
            }

    return render(request, 'website/projects/projects_list_view.html', context)

def projectDetails(request, slug=None):
        
        # projects_qs = Project.objects.all() #print(projects_qs)
        # projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
        # projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
        # projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
       
        
        context = {
                # 'projects_list': projects_qs,
                # 'projectcategories_list':projectCategories_qs,
                # 'projectcategories_list_1':projectCategories_qs_1,
                # 'projectcategories_list_2':projectCategories_qs_2,
                
            }
        
        # project_obj = None
        # if slug is not None:
        #     # project_obj = Project.objects.get(slug=slug)
        #     # project_obj = Project.objects.get(slug=slug)
        #     # project_lead = ProjectLead.objects.all()
        #     # project_qs = Project.objects.all()
        
        # context = {
        #     # 'project' : project_obj,
        #     # 'project_lead':project_lead,
        #     # 'project_list':project_qs
        # }
        
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

def projectsFilms(request):
        
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

def projectCategories(request, slug = None):
    
    projects_qs = Project.objects.all()#print(projects_qs)
    projectCategories_qs = Categories.objects.all()#print(projectCategories_qs)
    projectCategories_qs_1 = Categories.objects.all()[:5]#print(projectCategories_qs)
    projectCategories_qs_2 = Categories.objects.all()[5:]#print(projectCategories_qs)
        
    projectCategory = None
    if slug is not None:
        projectCategory = Categories.objects.get(slug=slug)
    
    context = {
            'projects_list': projects_qs,
            'projectcategories_list':projectCategories_qs,
            'projectcategories_list_1':projectCategories_qs_1,
            'projectcategories_list_2':projectCategories_qs_2,
            'Categories' : projectCategory,
    }

    return render(request, 'website/projects/project_categories/project_categories_home_view.html', context)

def projectCategoriesList(request):
    
#     projectCategories = Categories.objects.all()
    
    context = {
#         'project-categories-list' : projectCategories
    }

    return render(request, 'website/projects/project_categories/project_categories_list_view.html', context)

def projectCategoriesDetails(request, slug = None):
    
    # projects_qs = Project.objects.all()#print(projects_qs)
    # project_categories_qs = Categories.objects.all()#print(project-categories_qs)
    # project_categories_qs_1 = Categories.objects.all()[:5]#print(project-categories_qs)
    # project_categories_qs_2 = Categories.objects.all()[5:]#print(project-categories_qs)
        
    # projectCategory = None
    # if slug is not None:
    #     projectCategory = Categories.objects.get(slug=slug)

    context = {
            # 'Categories' : projectCategory,
            # 'projects_list': projects_qs,
            # 'project_categories_list':project_categories_qs,
            # 'project-categories_list_1':project_categories_qs_1,
            # 'project-categories_list_2':project_categories_qs_2         
    }

   

    return render(request, 'website/projects/project_categories/project_categories_detail_view.html', context)

def projectSubCategories(request, id=None):
        
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

def blank_Page(request):

    tree = 'It is getiing interesting' 

    context = {
        'variable' : tree
    } 

    return render(request,'website/misc/blank_page.html', context)

def blank_Template(request):

    tree = 'It is getiing interesting' 

    context = {
        'variable' : tree
    } 

    return render(request,'website/misc/blank_template_page.html', context)

def policies_and_guidelines(request):

    tree = 'It is getiing interesting' 

    context = {
        'variable' : tree
    } 

    return render(request,'website/misc/policies_and_guidelines.html', context)

def privacy_statement(request):

    tree = 'It is getiing interesting' 

    context = {
        'variable' : tree
    } 

    return render(request,'website/misc/privacy_statement.html', context)
""" Misc. End """