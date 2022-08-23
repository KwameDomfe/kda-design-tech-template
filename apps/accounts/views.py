from django.shortcuts import render

# Create your views here.

""" Accounts Page start """
def accounts(request):
   
    context = {
           
        }

    return render(request,'accounts/accounts-home.html', context)
""" Accounts Page end """

