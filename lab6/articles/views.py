from django.shortcuts import render, redirect
from .models import Article
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def archive(request):
    return render(request, 'archive.html', {'posts': Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {'post': post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous:
        pass
        if request.method == 'POST':
            form = {'text': request.POST['text'], 'title': request.POST['title']}


            # Проверка, что название статьи уникальное
            if Article.objects.filter(title=request.POST['title']).count():
                form['errors'] = u'Статья с таким названием уже существует!'
                return render(request, 'create_post.html', {'form': form})


            if form['text'] and form['title']:
                article = Article(text=form['text'], title=form['title'], author=request.user)
                article.save()
                return redirect('get_article', article_id=article.id)
            else:
                form['errors'] = u'Не все поля заполнены'
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html')
    else:
        raise Http404


def register(request):
    if request.method == 'POST':
        form = {'username': request.POST['username'], 'password': request.POST['password'], 'email': request.POST['email']}
        pass
        if not form['username']:
            form['errors'] = u'Имя пользователя не задано.'
            return render(request, 'register.html', {'form': form})

        if not form['email']:
            form['errors'] = u'Электронная почта пользователя не задана.'
            return render(request, 'register.html', {'form': form})

        if not form['password']:
            form['errors'] = u'Пароль пользователя не задан.'
            return render(request, 'register.html', {'form': form})


        if User.objects.filter(username=form['username']).count():
            form['errors'] = u'Пользователь с таким именем уже существует!'
            return render(request, 'register.html', {'form': form})


        user = User.objects.create_user(username=form['username'], email=form['email'], password=form['password'])

        login(request, user)
        return redirect('archive')
    else:
        return render(request, 'register.html')



def auth(request):
    if request.method == 'POST':
        form = {'username': request.POST['username'], 'password': request.POST['password']}

        user = authenticate(username=form['username'], password=form['password'])

        if user:
            login(request, user)
            return redirect('archive')

        else:
            form['errors'] = u'Такого аккаунта не существует!'
            return render(request, 'auth.html', {'form': form})
    else:
        return render(request, 'auth.html')


def log_out(request):
    logout(request)
    return redirect('archive')
