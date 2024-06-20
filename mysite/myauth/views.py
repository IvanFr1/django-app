from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.


class AboutMeView(LoginRequiredMixin, TemplateView):
    template_name = 'myauth/about-me.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class UpdateProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ['bio', 'avatar']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('myauth:users-list')

    def get_object(self, queryset=None):
        # Проверяем, есть ли у пользователя профиль, иначе создаем его
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user
    

class UsersListView(ListView):
    template_name = 'myauth/users_list.html'
    # model = Product
    context_object_name = 'users'
    def get_queryset(self):
        return User.objects.all()
    


class UserDetailsView(UserPassesTestMixin, DetailView):
    model = User
    template_name = 'myauth/user_details.html'  # Убедитесь, что этот путь корректен

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_pk = self.kwargs.get('pk')
        profile_user = get_object_or_404(User, pk=user_pk)
        context['profile_user'] = profile_user
        return context
    
    def test_func(self):
        user = self.request.user
        profile_user = self.get_object()
        return user.is_staff or user == profile_user # type: ignore

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs['pk'])
    

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:about-me')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object) # type: ignore
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/admin')
        
        return render(request, 'myauth/login.html')

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/admin')
    
    return render(request, 'myauth/login.html', {'error': 'Invalid login credentials'})


class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('myauth:login')


def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse('myauth:login'))

@user_passes_test(lambda u: u.is_superuser)
def set_cookie(request: HttpRequest) -> HttpResponse:
    response = HttpResponse('Cookie set')
    response.set_cookie('fizz', 'buzz', max_age=3600)
    return response

def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get('fizz', 'default value')
    return HttpResponse(f'Cookie value: {value!r}')

@permission_required('myauth.view_profile', raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session['foobar'] = 'spameggs'
    return HttpResponse('Session set!')


@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get('foobar', 'default')
    return HttpResponse(f'Session value: {value!r}')


class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({'foo': 'bar', 'spam': 'eggs'})
