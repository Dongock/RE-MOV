from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect, render_to_response
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages

from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('accounts/user_activate_email.html',{
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
            'token': account_activation_token.make_token(user),
            })
            mail_subject = "[ReVue] 회원가입 인증 메일입니다."
            to_email = user.email
            email = EmailMessage(mail_subject,message, to=[to_email])
            email.send()
            messages.success(request, '작성하신 이메일 주소로 인증용 이메일이 발송되었습니다. 인증 완료 후 서비스가 이용가능합니다.')
            return redirect("movies:index")
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html',context)

def activate(request, uid64, token):
    User = get_user_model()
    uid = force_text(urlsafe_base64_decode(uid64))
    print(uid)
    user = User.objects.get(pk=uid)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth_login(request, user)
        messages.success(request, '인증이 완료되었습니다. 이제부터 Revue 서비스를 이용하실 수 있습니다.')
        return redirect('movies:firstchoice')
    else:
        return HttpResponse('비정상적인 접근입니다.')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("movies:index")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.pk)
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:index')

def profile(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    context = {
        'user':user,
    }
    return render(request, 'accounts/profile.html',context)

def follow(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    if user != request.user:
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
    return redirect('accounts:profile', user.pk)