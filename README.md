 #Django Login & Register

Bu Django loyihasi foydalanuvchilar uchun login va register funksiyalarini taqdim etadi.

📌 Talablar

Python 3.8+

Django 4+

virtualenv (ixtiyoriy)

🔧 O'rnatish

Repository-ni klonlash

git clone <repository-url>
cd <project-folder>

Virtual muhit yaratish va faollashtirish (ixtiyoriy)

python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate  # Windows

Kerakli kutubxonalarni o‘rnatish

pip install -r requirements.txt

Ma'lumotlar bazasini yaratish

python manage.py migrate

Superuser yaratish (ixtiyoriy, admin panel uchun)

python manage.py createsuperuser

So‘ngra foydalanuvchi nomi, email va parolni kiriting.

Serverni ishga tushirish

python manage.py runserver

🔑 Login va Ro‘yxatdan o‘tish (Register)

📌 URL-lar

Register: http://127.0.0.1:8000/register/

Login: http://127.0.0.1:8000/login/

Logout: http://127.0.0.1:8000/logout/

📜 Views (Misol sifatida)

Register View

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

Login View

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = "login.html"

🎨 HTML Shablonlar

register.html

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Ro‘yxatdan o‘tish</button>
</form>

login.html

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Kirish</button>
</form>

📌 Qo‘shimcha

Agar foydalanuvchi tizimga kirgan bo‘lsa, logout qilish uchun:

<a href="{% url 'logout' %}">Chiqish</a>

Admin panelga kirish: http://127.0.0.1:8000/admin/

🤝 Hissa qo‘shish

Agar loyihaga qo‘shimcha qo‘shmoqchi bo‘lsangiz, pull request yuborishingiz mumkin.

📜 Litsenziya

Ushbu loyiha MIT litsenziyasi asosida tarqatiladi.
 
 
