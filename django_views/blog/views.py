from django.shortcuts import render, Http404, get_object_or_404, HttpResponseRedirect
from .models import PostModel
from .forms import PostModelForm
from django.contrib import messages
from django.db.models import Q

# Create your views here


def list_posts(request):
    if request.user.is_authenticated:
        print(f"{request.user} is authenticated")
    else:
        print("Not authenticated")
    search_title = request.GET.get("title")
    if search_title:
        posts = PostModel.objects.filter(
            Q(title__icontains=search_title) |
            Q(content__icontains=search_title) |
            Q(slug__icontains=search_title)
        )
    else:
        posts = PostModel.objects.all()
    context = {
        "posts": posts
    }

    return render(request, "blog/list-posts.html", context)


def read_post(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    context = {
        "obj": obj
    }
    return render(request, "blog/read-post.html", context)


def update_post(request, id=None):
    print(f"Checking what i get in id {id}")
    obj = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        print(f"The object that i am going to save is {form.cleaned_data}")
        obj.save()
        messages.success(request, f"Updated object with id {id}")
        return HttpResponseRedirect(f"/blog/read/{id}")
    context = {
        "form": form
    }
    return render(request, "blog/update-post.html", context)


def create_post(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        print(f"The object that i am going to save is {form.cleaned_data}")
        obj.save()
        messages.success(request, "Post successfully created")
        form = PostModelForm()
    context = {
        "form": form
    }
    return render(request, "blog/create-post.html", context)


def delete_post(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    if request.method == "POST":
        print("Deleting object ..")
        obj.delete()
        messages.success(request, f"Post deleted with id {id}")
        return HttpResponseRedirect("/blog/posts")
    context = {
        "obj": obj
    }
    return render(request, "blog/delete-post.html", context)
