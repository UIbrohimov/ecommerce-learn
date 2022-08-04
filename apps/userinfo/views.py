from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from .forms import SignUpForm


# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=True)
#             login(request, user) 
#             messages.success(request, 'Tizimga muvoffaqiyatli kirdingiz')
#             return redirect('poll:savollar')
#     return render(request, 'userprofile/register.html', {'form': SignUpForm()})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'userinfo/register.html'
    success_url = revese_lazy('login')

    def get_contex_data(self, *, object_list=None, **kwargs):
        context = super().get_contex_data(**kwargs)
        c_def = self.get_user_context(title="Royxatdan o'tish")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LodinView):
    form_class = AuthenticationForm
    template_name = 'userinfo/login.html'

    def get_contex_data(self, *, object_list=None, **kwargs):
        context = super().get_contex_data(**kwargs)
        c_def = self.get_user_context(title="Tizimga kirish")
        return dict(list(context.items()) + list(c_def.items()))