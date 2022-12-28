from django.shortcuts import render,redirect
from django.contrib.auth import logout
# Create your views here.


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/") #give path to after logout page
    return render(request,"",{}) # give path to what page to render in 2nd argument
