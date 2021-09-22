
from django.shortcuts import redirect, render
from .models import Short_urls
from .form import UrlForm
from .shorter import  Shortner

# Create your views here.
def Home(request,token):
    long_url =Short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url) 

def Make(request):
    form = UrlForm(request.POST)
    a = ""
    if request.method == 'POST':
        if form.is_valid():
            NewUrl=form.save(commit=False)
            a =Shortner().issue_token()
            NewUrl.Short_urls =a
            NewUrl.save()
        else:
            form =UrlForm()
            a="Invalid URL"
    return render(request,'home.html',{'form':form ,'a':a})
