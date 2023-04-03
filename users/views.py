from django.shortcuts import render, redirect

from users.forms import LoginForms, RegisterForm

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages

# Create your views here.
def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()

        user = auth.authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'{username} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'users/login.html', {'form': form})

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username=form['username'].value() 
            email=form['email'].value()
            password=form['password_1'].value() 

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro') 

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save() 

            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')

    return render(request, 'users/register.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')