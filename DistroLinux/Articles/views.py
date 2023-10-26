from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Articles.models import Article, Profile
from Articles.forms import ArticleForm, NewUserForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

# themes_list = {"Linux": ["Ubuntu", "Mint", "Debian", "Fedora", "Manjaro", "Other_Distro"],
#                "Linux Gaming": ["Native_Gaming", "Proton", "Wine"]}


ARTICLES_ON_SCREEN = 5


def index(request):
    # global themes_list

    # theme_list_counter = {"Ubuntu": Article.objects.filter(theme="Ubuntu").count(),
    #                       "Mint": Article.objects.filter(theme="Mint").count(),
    #                       "Debian": Article.objects.filter(theme="Debian").count(),
    #                       "Fedora": Article.objects.filter(theme="Fedora").count(),
    #                       "Manjaro": Article.objects.filter(theme="Manjaro").count(),
    #                       "Other_Distro": Article.objects.filter(theme="Other_Distro").count(),
    #                       "Native_Gaming": Article.objects.filter(theme="Native_Gaming").count(),
    #                       "Proton": Article.objects.filter(theme="Proton").count(),
    #                       "Wine": Article.objects.filter(theme="Wine").count(),
    #                       }

    context = {
        "articles": Article.objects.all(),
        # "categories": themes_list,
        # "theme_list_counter": theme_list_counter,
    }

    # return render(request, "Articles/articles_main.html", context=context)
    return redirect('show-pages', page_id=1)


def show_article(request, theme, article_pk):
    # theme_list_counter = {"Ubuntu": Article.objects.filter(theme="Ubuntu").count(),
    #                       "Mint": Article.objects.filter(theme="Mint").count(),
    #                       "Debian": Article.objects.filter(theme="Debian").count(),
    #                       "Fedora": Article.objects.filter(theme="Fedora").count(),
    #                       "Manjaro": Article.objects.filter(theme="Manjaro").count(),
    #                       "Other_Distro": Article.objects.filter(theme="Other_Distro").count(),
    #                       "Native_Gaming": Article.objects.filter(theme="Native_Gaming").count(),
    #                       "Proton": Article.objects.filter(theme="Proton").count(),
    #                       "Wine": Article.objects.filter(theme="Wine").count(),
    #                       }

    current_article = Article.objects.filter(theme=theme).filter(pk=article_pk)
    content = {"current_article": current_article,
               # "categories": themes_list,
               # "theme_list_counter": theme_list_counter,
               }
    return render(request, "Articles/show_arcticle.html", context=content)
    # return HttpResponse(f"<h1>{article_pk}</h1")


def open_theme_page(request, theme, page_id):
    # theme_list_counter = {"Ubuntu": Article.objects.filter(theme="Ubuntu").count(),
    #                       "Mint": Article.objects.filter(theme="Mint").count(),
    #                       "Debian": Article.objects.filter(theme="Debian").count(),
    #                       "Fedora": Article.objects.filter(theme="Fedora").count(),
    #                       "Manjaro": Article.objects.filter(theme="Manjaro").count(),
    #                       "Other_Distro": Article.objects.filter(theme="Other_Distro").count(),
    #                       "Native_Gaming": Article.objects.filter(theme="Native_Gaming").count(),
    #                       "Proton": Article.objects.filter(theme="Proton").count(),
    #                       "Wine": Article.objects.filter(theme="Wine").count(),
    #                       }

    context = {"articles": Article.objects.filter(theme=theme),
               "current_theme": theme,
               "page_id": page_id,
               "articles_on_screen": ARTICLES_ON_SCREEN,
               # "categories": themes_list,
               # "theme_list_counter": theme_list_counter,

               }

    # print('content.count =', Article.objects.filter(theme=theme).count())

    return render(request, 'Articles/articles_main.html', context=context)


@login_required(login_url="login-request")
def add_article(request):
    # global themes_list

    # theme_list_counter = {"Ubuntu": Article.objects.filter(theme="Ubuntu").count(),
    #                       "Mint": Article.objects.filter(theme="Mint").count(),
    #                       "Debian": Article.objects.filter(theme="Debian").count(),
    #                       "Fedora": Article.objects.filter(theme="Fedora").count(),
    #                       "Manjaro": Article.objects.filter(theme="Manjaro").count(),
    #                       "Other_Distro": Article.objects.filter(theme="Other_Distro").count(),
    #                       "Native_Gaming": Article.objects.filter(theme="Native_Gaming").count(),
    #                       "Proton": Article.objects.filter(theme="Proton").count(),
    #                       "Wine": Article.objects.filter(theme="Wine").count(),
    #                       }

    if request.method == "POST":
        record = Article()
        record.title = request.POST['title']
        record.author = request.POST['author']
        record.theme = request.POST['theme']

        record.content = request.POST['content']
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data.get("image")
            record.image = request.FILES['image']
            # record.theme = "Linux"

        record.save()

        return redirect('main')
    else:
        add_new_article_context = {
            "article_form": ArticleForm,
            # "categories": themes_list,
            # "theme_list_counter": theme_list_counter,
        }

    return render(request, "Articles/articles-add-new.html", context=add_new_article_context)


def show_pages(request, page_id):
    context = {
        "articles": Article.objects.all(),
        "page_id": page_id,
        "articles_on_screen": ARTICLES_ON_SCREEN,
    }

    return render(request, "Articles/articles_main.html", context=context)


def show_register_page(request):
    if request.method == "POST":
        profile = request.user
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # current_user = User.objects.get(username=form.cleaned_data.get('username'),
            #                                 email=form.cleaned_data.get('email'))
            login(request, user)

            Profile.objects.filter(user=user).update(
                profile_image=request.FILES['profile_image'])  # , profile_image=request.FILES['profile_image'])
            messages.success(request, "Your account has been registered successfully!")
            return redirect('main')

    form = NewUserForm()
    return render(request, "Articles/register-form-page.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}.")
                return redirect("main")
            else:
                messages.error(request, "Invalid username or password.", extra_tags="message-box-login-error")
        else:
            messages.error(request, "Invalid username or password.", extra_tags="message-box-login-error")
    form = AuthenticationForm()
    return render(request=request, template_name="Articles/login-form.html", context={"login_form": form})


def logout_from_account(request):
    logout(request)
    # messages.info(request, "You have successfully logged out")
    return redirect('main')


def logged_user_page(request, user_pk, username):
    # current_user = User.objects.filter(pk=1)
    current_user_profile = Profile.objects.filter(user=user_pk) #.filter(username=username)
    print('hello', current_user_profile[0])
    # current_user_profile = request.user.profile

    # profile_form = ProfileForm(instance=current_user_profile)
    # print(current_user_profile)
    #
    # if request.method == "POST":
    #     profile_form = ProfileForm(request.POST, request.FILES, instance=current_user_profile)
    #
    #     if profile_form.is_valid():
    #         profile_form.save()

    return render(request=request, template_name="Articles/logged-userpage.html",
                  context={"current_user": current_user_profile[0]}) #,
                           # "profile_form": profile_form})


@login_required(login_url='login-request')
def change_profile(request, user_pk, username):
    current_user_profile = Profile.objects.filter(user=user_pk)  # .filter(username=username)
    logged_user = request.user.profile
    current_user_profile_id = current_user_profile.values('id').get()
    print('users', current_user_profile_id['id'], logged_user.id)
    if logged_user.id != current_user_profile_id['id']:
        print('Not Same Person!')
        return redirect('main')

    profile_form = ProfileForm(instance=logged_user)
    print(current_user_profile)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=logged_user)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('logged-user-page', user_pk=request.user.id, username=request.user.username)

    return render(request=request, template_name="Articles/change-profile-form.html",
                  context={"current_user": current_user_profile,
                           "profile_form": profile_form})
