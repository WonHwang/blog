from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.http import HttpResponseForbidden

def home(request):
    blogs = Blog.objects # 모델로부터 객체 목록을 받을 수 있다 ==> 이 목록을 쿼리셋이라고 한다.
    return render(request, 'home.html', {'blogs' : blogs})


    # 쿼리셋과 메소드의 형식
    # 모델이름.쿼리셋(objects).메소드 이런방식으로 사용한다.
    #ex) blogs.all() ==> blog로 만든 모든 쿼리셋을 가져온다.

def hello(request):
    return render(request, 'hello.html')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog' : blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        blog = Blog()
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.image = request.FILES['image']
        blog.save() #쿼리셋 메소드입니다. 객체를 저장하도록 하는 메소드입니다.
        return redirect('/blog/' + str(blog.id))
    return HttpResponseForbidden('allowed only via POST')
#render와 redirect의 차이점은?
#--> redirect는 url에 아무 url이나 입력가능함. 예를 들어 구글같은거도 입력가능함.