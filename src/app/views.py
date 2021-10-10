from django.shortcuts import redirect, render
from .models import *
from .forms import ResumeForm
from django.contrib import messages

# Create your views here.

def Home(request):
    candidates = Resume.objects.all()[:8]
    form = ResumeForm()
    if request.method == 'POST':
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Resume Uploaded Successfully')
            return redirect('/')
            
    context = {'form':form,'candidates':candidates}
    return render(request,'app/home.html',context)


def Candidate(request,pk):
    candidate = Resume.objects.get(id=pk)
    context = {'candidate':candidate}
    return render(request,'app/candidate.html',context)

def CandidateList(request):
    candidates = Resume.objects.all()
    context = {'candidates':candidates}
    return render(request,'app/candidateList.html',context)