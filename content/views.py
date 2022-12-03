from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,reverse
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from content.models import *
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from content.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class MyPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise


def BlogList(request):
    obj = Blog.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(obj, 5)
    try:
        blog_lists = paginator.page(page)
    except PageNotAnInteger:
        blog_lists = paginator.page(1)
    except EmptyPage:
        blog_lists = paginator.page(paginator.num_pages)
    context = {
        'objects_list':blog_lists
    }
    return render(request,'index.html',context)


def BlogDetailView(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    comments = post.comment_post.all()

    if request.method == 'POST' and request.POST['action'] == "like":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            form = comment_form.save(commit=False)
            form.post = post
            form.save()
    elif request.method == 'POST' and request.POST['action'] == "comment":
        data = request.POST
        comment = Comment.objects.get(id = data["id"])
        user = User.objects.get(id = request.user.id)
        comment.likes.add(user)
        comment.save()

    elif request.method == 'POST' and request.POST['action'] == "email":
        email_form = NewsLetterForm(data=request.POST)
        if email_form.is_valid():
            email_form.save()

    comment_form = CommentForm()
    email_form = NewsLetterForm()


    context = {
        'object' : post,
        'comments': comments,
        'comment_form': comment_form,
        'email_form':email_form
    }
    return render(request,'blog/blog_detail.html',context)     


class BlogUpdateView(UpdateView):
    model = Blog
 
    fields = [
        "title",
        "description"
    ]
 
    success_url ="/"

class BlogDeleteView(DeleteView):
    model = Blog
    success_url ="/"