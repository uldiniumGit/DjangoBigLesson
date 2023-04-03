from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(label='название')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='сообщение')


class NewsForm(forms.Form):
    title = forms.CharField(label='Название новости', max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    video_link = forms.CharField(label='Ссылка на видео')
