from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def post_list(request):
    posts=Post.objects.order_by('-id')
    return render(request, 'test1/post_list.html',{'posts':posts})

def add_list(request):
    return render(request, 'test1/add_list.html',{})

def registerPost(request):
    p=Post(title=request.POST['title'],
           text=request.POST['text'])
    p.save()
    return post_list(request)

def deletePost(request,post_id):
    p=Post.objects.get(id=post_id)
    p.delete()
    return HttpResponse("삭제되었습니다!.")

def detailPost(request, post_id):
    post=Post.objects.get(id=post_id)
    return render(request, 'test1/detailPost.html',{'post':post})

def editPost(request,post_id):
    post=Post.objects.get(id=post_id)
    return render(request, 'test1/editPost.html',{'post':post})

def edit(request,post_id):
        p = Post.objects.get(id=post_id)
    # 글을 수정사항을 입력하고 제출을 눌렀을 때
        if request.method == "POST":
            form = Post(request.POST, request.FILES)
                # {'name': '수정된 이름', 'image': <InMemoryUploadedFile: Birman_43.jpg 	(image/jpeg)>, 'gender': 'female', 'body': '수정된 내용'}
            print(form.cleaned_data)
            p.name = form.cleaned_data['title']
            p.image = form.cleaned_data['text']
            p.save()
            return HttpResponse("변경되었습니다.")

    # 수정사항을 입력하기 위해 페이지에 처음 접속했을 때
        else:
            form = CatPost()
            return HttpResponse("변경되었습니다.")
