from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse

#ADMIN LOGIN
def userlogin_view(request):

    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')#print(username, password)
        user = authenticate(
            request, 
            username=username,
            password=password)
        if user is None:
            context ={'error': 'Invalid Username or Password'
            }
            return render(request,'accounts/user-login.html', context
            )
        login(request, user)
        return redirect('/admin')
    context = {

    }
    return render(request,'accounts/user-login.html', context)

def userlogout_view(request):
    if request.method =='POST':
        logout(request)
        return redirect('/accounts/user-login')
    context = {

    }
    return render(request,'accounts/user-logout.html', context)

def userRegister_view(request):
    context = {

    }
    return render(request,'accounts/register.html', context)

# def admin_Login(request):
#     context = {

#     }
#     return render(request,'accounts/admin-login.html', context)

# def staff_Login(request):
#     context = {

#     }
#     return render(request,'accounts/staff-login.html', context)

# def admin_Home(request):
#     context = {

#     }
#     return render(request,'accounts/admin-home.html', context)

# def admin_Login_Process(request):

#     username=request.POST.get('username')
#     password=request.POST.get('password')
#     print(username,password)

#     user=authenticate(
#         request=request, 
#         username=username, 
#         password=password,
#     )
#     print(user)
    
#     if user is not None:
#         login(request=request, user=user)
#         return HttpResponseRedirect(reverse('admin-login'))
#     else:
#         messages.error(request, 'Invalid Credentials')
#         return HttpResponseRedirect(reverse('accounts:admin-home'))
    

