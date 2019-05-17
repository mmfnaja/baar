from django.shortcuts import render, redirect
from account.forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
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
