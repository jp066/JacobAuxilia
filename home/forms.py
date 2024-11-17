from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message', 'attachment']  # Inclua o campo 'attachment'
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Assunto'}),
            'message': forms.Textarea(attrs={'placeholder': 'Descreva sua dúvida ou sugestão'}),
        }
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(FeedbackForm, self).__init__(*args, **kwargs)
        
        if user and user.is_authenticated:
            self.fields['name'].initial = user.username
            self.fields['email'].initial = user.email
            self.fields['name'].disabled = True
            self.fields['email'].disabled = True


class VideoSearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False, label="Pesquisar por título")