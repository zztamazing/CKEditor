from django import forms
from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingFormField
from .models import Passage

class editPassageForm(forms.ModelForm):
    content = RichTextUploadingFormField(label='内容',config_name = 'default')

    class Meta:
        model = Passage
        fields = ['content', ]