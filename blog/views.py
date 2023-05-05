from django.shortcuts import render,HttpResponseRedirect
from .forms import sigupform,loginform,postform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . models import post
from django.contrib.auth.models import Group

# HOME
def home(request):
    posts = post.objects.all()
    return render(request, 'blog/home.html',{'posts': posts})
#ABOUT
def about(request):
    return render(request, 'blog/about.html')
#CONTACT
def contact(request):
    return render(request, 'blog/contact.html')
#DASHBOARD
def dashboard(request):
    if request.user.is_authenticated:
     posts = post.objects.all()
     user = request.user
     full_name = user.get_full_name()
     gps = user.groups.all()
     return render(request, 'blog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps})
    else:
     return HttpResponseRedirect('/login/')
 
#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#SIGUP
def user_sigup(request):
    if request.method == "POST":
     form = sigupform(request.POST)
     if form.is_valid():
      messages.success(request,'congrulations!!! you have become an Author')
      user = form.save()
      group = Group.objects.get(name='Author')
      user.groups.add(group)
    else:
     form = sigupform()
    return render(request,'blog/signup.html',{'form':form})
#login
def user_login(request):
      if request.method =="POST":
       form = loginform(request=request, data=request.POST)
       if form.is_valid():
        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user = authenticate(username=uname,password=upass)
        if user is not None:
         login(request,user)
         messages.success(request,'logged in successfully !!!')
        return HttpResponseRedirect('/dashboard/')   
      else:
        form = loginform()
      return render(request, 'blog/login.html',{'form':form})
  
  # add new post
def add_post(request):
    if request.user.is_authenticated:
     if request.method == 'POST':
         form=postform(request.POST)
         if form.is_valid():
          title = form.cleaned_data['title']
          description = form.cleaned_data['description']
          pst = post(title=title,description=description)
          pst.save() 
          messages.success(request,'Add successfully!!!!') 
         form = postform()     
     else:
      form = postform()           
     return render(request,'blog/addpost.html',{'form':form}) 
    else:
      return HttpResponseRedirect('/login/')
     

    
 
    # update post
def update_post(request,id):
   if request.user.is_authenticated:
     if request.method == 'POST':
        pi=post.objects.get(pk=id)
        form=postform(request.POST,instance=pi)
        if form.is_valid():
         messages.success(request,'update successfully!!!!') 
         form.save()
     else:
      pi=post.objects.get(pk=id)
      form=postform(instance=pi)         
     return render(request,'blog/updatepost.html',{'form':form}) 
   else: 
    return HttpResponseRedirect('/login/') 
    
       # delete  post
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = post.objects.get(pk=id)
            pi.delete() 
        return HttpResponseRedirect('/dashboard/') 
    else:
        return HttpResponseRedirect('/login/')    
    
   
    


    
      

    



