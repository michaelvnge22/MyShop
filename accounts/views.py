from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect

User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Vérifier si l'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            return render(request, "accounts/signup.html", {"error": "Nom d'utilisateur déjà pris"})

        # Créer l'utilisateur s'il n'existe pas
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('index')

    return render(request, 'accounts/signup.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {"error": "Nom d'utilisateur ou mot de passe incorrect"})

    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('index')
