from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views import View
from .forms import UserCreateForm, UserAuthenticateForm, AddListForm, AddItemToListForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth import authenticate, login, logout
from .models import List, Item


class MainPageView(LoginRequiredMixin, View):

    def get(self, request):
        lists = List.objects.all()
        items = Item.objects.all()
        ctx = {
            "lists": lists,
            "items": items
        }
        return render(request, 'base.html', ctx)


class ListView(View):

    def get(self, request, id):
        list = List.objects.get(pk=id)
        return render(request, 'list.html', {'list': list},
                                            {'list_title': list.title})


class RegisterView(FormView):
    template_name = 'form.html'
    form_class = UserCreateForm
    success_url = '/login'

    def form_valid(self, form):
        u = User()
        u.username = form.cleaned_data['username']
        u.first_name = form.cleaned_data['first_name']
        u.last_name = form.cleaned_data['last_name']
        u.email = form.cleaned_data['email']
        u.set_password(form.cleaned_data['password'])
        u.save()

        return super(RegisterView, self).form_valid(form)


class LoginView(View):

    def get(self, request):
        form = UserAuthenticateForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = UserAuthenticateForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["user"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect('/main')
            else:
                return redirect('/login')


class LogoutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        return redirect('/login')


class AddListView(LoginRequiredMixin, FormView):

    def get(self, request):
        form = AddListForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddListForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                l = List()
                l.title = form.cleaned_data['title']
                l.user_id = request.user.id
                l.save()
                return redirect('/main')


class DeleteListView(LoginRequiredMixin, View):

    def get(self, request, list_id):
        l = List.objects.get(pk=list_id, user_id=request.user.id)
        l.delete()
        return redirect('/main')


class AddItemToListView(LoginRequiredMixin, View):

    def get(self, request, list_id):
        list = List.objects.get(pk=list_id)
        form = AddItemToListForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request, list_id):
        list = List.objects.get(pk=list_id)
        form = AddItemToListForm(request.POST)
        if form.is_valid():
            i = Item()
            i.title = form.cleaned_data['title']
            i.priority = form.cleaned_data['priority']
            i.completed = form.cleaned_data['completed']
            i.list_id = list.id
            i.save()
            return redirect('/main')


class DeleteItemFromListView(LoginRequiredMixin, View):

    def get(self, request, item_id):
        i = Item.objects.get(pk=item_id)
        i.delete()
        return redirect('main')
