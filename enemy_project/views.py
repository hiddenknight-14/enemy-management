from django.shortcuts import redirect, render
from enemies.models import Enemy

def home(request):

    revenge_taken_enemies = Enemy.objects.filter(revenge_taken=True).order_by('-updated_at')
    revenge_not_taken_enemies = Enemy.objects.filter(revenge_taken=False).order_by('-updated_at')

    context = {
        'revenge_taken_enemies': revenge_taken_enemies,
        'revenge_not_taken_enemies': revenge_not_taken_enemies,
    }

    return render(request, 'enemy_home.html', context=context)



# Manual credentials
ALLOWED_USER = {
    "username": "root",
    "password": "root"
}

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == ALLOWED_USER["username"] and password == ALLOWED_USER["password"]:
            request.session["logged_in"] = True
            return redirect("enemy-home")  # redirect to homepage
        else:
            return render(request, "enemy-login.html", {"error": True})  # trigger modal

    return render(request, "enemy-login.html")