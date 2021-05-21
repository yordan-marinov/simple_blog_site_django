from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
        "page_title": "posts",
        "form_type": "posts list",
    }
    return render(request, "post_list.html", context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        "post": post,
        "page_title": "details",
        "form_type": "post details",
    }
    return render(request, "post_detail.html", context)


def post_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/posts")

    context = {
        "form": form,
        "page_title": "create form",
        "form_type": "create",
    }
    return render(request, "post_create.html", context)


def post_update(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/posts")

    context = {
        "form": form,
        "page_title": "update form",
        "form_type": "update",
    }
    return render(request, "post_create.html", context)


def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return HttpResponseRedirect("/posts")
