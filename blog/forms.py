from django import forms
from .models import Post
# from django.contrib.admin import widgets
# from django.forms import widgets

class PostForm(forms.ModelForm):
    # published_date=forms.DateField(widgets=DateInput())
    class Meta:
        model = Post
        fields = ['title','text','published_date']
    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['published_date'].widget = widgets.AdminSplitDateTime()
