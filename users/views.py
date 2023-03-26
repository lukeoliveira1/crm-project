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
            # pegando valores do form
            username = form['username'].value()
            password = form['password'].value()

        # método que autentica um usuário, pode retornar True ou None
        user = auth.authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            auth.login(request, user) # faz login
            messages.success(request, f'{username} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'users/login.html', {'form': form})

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        #recebendo os dados passados em um novo form
        form = RegisterForm(request.POST)

        # validando formulário
        if form.is_valid():
            username=form['username'].value() #mesmo nome utilizado no form.py
            email=form['email'].value()
            password=form['password_1'].value() #puxando info do form

            # verificando se o usuário já existe
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro') # redireciona pra página de cadastro

            # criando usuário
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save() # salvando

            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')

    return render(request, 'users/register.html', {'form': form})

def logout(request):
    # fazendo logout
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')