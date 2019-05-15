from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileUpdateForm
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

    def myaccount(request):
        template_name = 'profile.html'
        if request.method == 'POST':
            form = ProfileUpdateForm(request.POST, instance=request.user.staff)
            if form.is_valid():
                form.save()
                return redirect('/myaccount')
        else:
            form = ProfileUpdateForm(instance=request.user.staff)
        context={
            'form':form
        }
        return render(request, template_name, context)
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
