from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from RealEstate.models import RealEstate
from RealEstate.models import Categories
from .forms import RealestateForm, UserRegisterForm, UserLoginForm, ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.mail import send_mail


def test(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'STest155@yandex.ru', ['sarmatdzivaev@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')
    else:
        form = ContactForm()
    return render(request, 'RealEstate/test.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user =  form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()

    return render(request, 'RealEstate/registration.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Введите правильные данные')

    else:
        form = UserLoginForm()
    return render(request, 'RealEstate/login.html', {'form': form})


class HomeRealEstate(ListView):
    model = RealEstate
    context_object_name = 'realobjects'
    paginate_by = 2

    def  get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Недвижимость'
        return context
    def get_queryset(self):
        return RealEstate.objects.all().select_related('category')


class EstateCat(ListView):
    model = RealEstate
    context_object_name = 'realobjects'
    template_name = 'RealEstate/getcat.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Categories.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return RealEstate.objects.filter(category_id = self.kwargs['category_id'])


class CreateEstate(LoginRequiredMixin, CreateView):
    form_class = RealestateForm
    template_name = 'RealEstate/add_realestate.html'
    success_url = reverse_lazy('home')
    login_url = '/admin'

class ViewRealEstate(DetailView):
    model = RealEstate
    context_object_name = 'definite_realestate'
    template_name = 'RealEstate/view_realestate.html'

def nyy(request):
    realobjects = RealEstate.objects.all()
    categories = Categories.objects.all()
    return render(request, 'RealEstate/nyy.html', {'realobjects': realobjects, 'realobject':
                                                   'Недвижимость', 'categories': categories})
def get_category(request, category_id):
    n = RealEstate.objects.filter(category_id=category_id)
    hhh = RealEstate.objects.all()
    j = RealEstate.objects.get(pk=category_id)
    category = Categories.objects.all()
    c = Categories.objects.get(pk=category_id)
    return render(request, 'RealEstate/cat.html', {'n': n, 'hhh': hhh, 'j': j, 'category': category, 'c':c})


def view_realestate(request, id):
    definite_realestate= get_object_or_404(RealEstate,pk=id)
    return render(request, 'RealEstate/view_realestate.html', {'definite_realestate':definite_realestate})


def add_realestate(request):
    if request.method =='POST':
        form = RealestateForm(request.POST)
        if form.is_valid():
            #RealEstate.objects.create(**form.cleaned_data)
            realestate = form.save()
            return redirect('home')
    else:
        form = RealestateForm()
    h = RealEstate.objects.all()
    return render(request, 'RealEstate/add_realestate.html', {'form':form, 'h':h})