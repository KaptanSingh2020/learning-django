from django.http import HttpResponseRedirect
from django.shortcuts import redirect
# from blog.urls import blog_post_list

# def redirect_root(request):
#     return HttpResponseRedirect('/blog/')

# def redirect_root(request):
#     return redirect('/blog/')

def redirect_root(request):
    return redirect('blog_post_list')
