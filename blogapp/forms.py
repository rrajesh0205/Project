import django
from blogapp.models import Article
from . models import Article



class PostForm(django.forms.ModelForm):

    def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Article
        fields = ('title', 'body', 'img')
        labels = {'title': 'Blog Title', 'body': 'Content of the Blog', 'img': 'Any Image related to the Content'}
