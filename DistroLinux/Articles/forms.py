from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # profile_image = forms.ImageField(required=False)

    class Meta:
        model = User
        # "profile_image"
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        # user.profile_image = self.cleaned_data['profile_image']
        # AdditionalUserInfo(user=user.id, profile_image=self.cleaned_data["profile_image"]).save()
        # profile_image = self.cleaned_data["profile_image"]

        if commit:
            user.save()

        return user


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


class ArticleForm(forms.Form):
    required_css_class = "add-article-form"

    themes_list = [("Ubuntu", "Ubuntu"),
                   ("Mint", "Mint"),
                   ("Debian", "Debian"),
                   ("Fedora", "Fedora"),
                   ("Manjaro", "Manjaro"),
                   ("Other_Distro", "Other Distro"),
                   ("Native_Gaming", "Native Gaming"),
                   ("Proton", "Proton"),
                   ("Wine", "Wine")]

    title = forms.CharField(widget=forms.TextInput(attrs={"class": "field form-elem"}), label="Title", max_length=255)
    author = forms.CharField(widget=forms.TextInput(attrs={"class": "field form-elem"}), label="Author", max_length=100)
    theme = forms.CharField(label="Theme",
                            widget=forms.Select(choices=themes_list, attrs={"class": "field form-elem"}))
    image = forms.ImageField()
    # "rows":15, "cols":80
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={"class": "text-area form-elem", }))
