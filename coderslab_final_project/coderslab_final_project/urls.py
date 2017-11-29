"""coderslab_final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from coderslab import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main', views.MainPageView.as_view(), name='main'),
    url(r'^list/(?P<id>(\d)+)', views.ListView.as_view(), name='list-id'),
    url(r'^register', views.RegisterView.as_view(), name='register'),
    url(r'^login', views.LoginView.as_view(), name='login'),
    url(r'^logout', views.LogoutView.as_view(), name='logout'),
    url(r'^add_list', views.AddListView.as_view(), name='add-list'),
    url(r'^delete/(?P<list_id>(\d)+)', views.DeleteListView.as_view(), name='delete'),
]
