from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic
from .models import *


from django.contrib.auth.decorators import login_required

@login_required
class Main():
    login_url = 'login/'
    def index(request):

        template_name = "index.html";
        return render(request, template_name)

    def login(request):

        template_name = "index.html";
        return render(request, template_name)

    def chatroom(request):

        template_name = "chatroom.html";
        return render(request, template_name)

    def myaccount(request, pk=None):
        template_name = 'profile.html'
        if pk:
            user = User.objects.get(pk=pk)
        else:
             user = request.user
        args = {'user': user}
        return render(request, template_name, args)
    
    #def project(request):
    #    template_name = 'project.html'
    #    return render(request, template_name) 


    # def specific(request):
    #     value = request.GET["id"]
    #     brand = Brand.objects.get(pk=value)
    #     model = Model.objects.filter(brand = brand)
    #
    #
    #     obj = Brand.objects.all()
    #     return render(request, 'model.html', {'obj' :obj, 'model' :model})
    #
    # def details(request):
    #
    #     obj = Brand.objects.all()
    #     value = request.GET["id"]
    #     model = Model.objects.get(pk=value)
    #
    #     review = Review.objects.filter(model = model)
    #     newslink = Newslink.objects.filter(model=model)
    #
    #     return render(request, 'review.html', {'obj' :obj,
    #                                            'newslink' :newslink,
    #                                            'review' :review})

class ProjectListView(generic.ListView):
    template_name = 'project.html'
    context_object_name = 'all_projects'

    def get_queryset(self):
        return project.objects.all()