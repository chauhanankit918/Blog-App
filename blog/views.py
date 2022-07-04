from django.shortcuts import render,redirect
from blog.models import blogs
from blog.forms import blogForm

# Create your views here.
def home(request):
    AllBlogs=blogs.objects.all()
    context={
        'blogs':AllBlogs,
    }
    print(AllBlogs)
    return render(request,'home.html',context)

def addBlog(request):
    form=blogForm()
    if request.method=='POST':
        form=blogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form,
    }
    return render(request,'addblog.html',context)

def likeBlog(request,pk):
    blog=blogs.objects.get(id=pk)
    blog.likes+=1
    blog.save()
    return redirect('/')