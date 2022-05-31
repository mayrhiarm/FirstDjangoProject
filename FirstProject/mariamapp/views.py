from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ApplicantForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    submitted = False
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form = ApplicantForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'register.html', {'form': form, 'submitted': submitted})
    



