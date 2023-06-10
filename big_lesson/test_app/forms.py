from django import forms


class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=32, unique=True)
    img = forms.FileField(upload_to='clients', null=True, blank=True)
    link = forms.URLField()


class NewsForm(forms.Form):
    title = forms.CharField(max_length=32, unique=True)
    text = forms.CharField(max_length=32, unique=True)
    video_link = forms.CharField(max_length=32, unique=False)
    img1 = forms.FileField(upload_to='clients', null=True, blank=True)
    img2 = forms.FileField(upload_to='clients', null=True, blank=True)
    img3 = forms.FileField(upload_to='clients', null=True, blank=True)
    img4 = forms.FileField(upload_to='clients', null=True, blank=True)
    img5 = forms.FileField(upload_to='clients', null=True, blank=True)

# class ContactForm(forms.Form):
#     name = forms.CharField(label='имя')
#     email = forms.EmailField(label='email')
#     phone_number = forms.CharField(label='номер телефона')
#
#
# class NewsForm(forms.Form):
#     title = forms.CharField(label='Название новости', max_length=100)
#     text = forms.CharField(widget=forms.Textarea)
#     video_link = forms.CharField(label='Ссылка на видео', widget=forms.TextInput(
#         attrs={'placeholder': 'https://www.youtube.com/embed/id', 'class': 'form-control'}))
