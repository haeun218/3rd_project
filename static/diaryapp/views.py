from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .models import Diary
from .forms import DiaryForm

# Create your views here.
def main(request):
    posts = Diary.objects
    post_list = Diary.objects.all() #블로그 모든 글들을 대상으로
    paginator = Paginator(post_list, 2) #블로그 객체 3개를 한페이지로 자르기
    page = request.GET.get('page') #request된 page가 뭔지를 알아내고, key값이 page인 get으로 얻어낸 dictionary형 value값을 page라는 변수에 담아준다 ?
    episodes= paginator.get_page(page)
    return render(request, 'crud/main.html', {'posts': posts, 'episodes': episodes })

def show(request, post_id):
    post = get_object_or_404(Diary, pk = post_id )
    return render(request, 'crud/show.html', {'post': post})

def new(request):
    return render(request, 'crud/new.html')

def postcreate(request):
    if request.method =='POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('main')
    else: 
        form = DiaryForm()
        return render(request,'crud/new.html', {'form': form})

def edit(request):
    return render(request, 'crud/edit.html')

def postupdate(request, post_id):
    post = get_object_or_404(Diary, pk = post_id)
    if request.method == 'POST':
        form = DiaryForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('show', post_id=post.pk)
    else:
        form = DiaryForm(instance=post)
        return render(request, 'crud/edit.html', {'form': form})

def postdelete(request, post_id):
    post = get_object_or_404(Diary, pk = post_id)
    post.delete()
    return redirect('main')