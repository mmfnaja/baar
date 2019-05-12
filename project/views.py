from django.http import HttpResponse
from django.shortcuts import render


class Main():


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

        template_name = "profile.html";
        return render(request, template_name)


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
