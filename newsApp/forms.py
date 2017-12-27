from django.forms import ModelForm, Textarea
from .models import News
class AddNewsForm(ModelForm):
	# news_title = forms.CharField(label='Title', max_length=100)
	# news_desc = forms.CharField(label='Body', max_length=5000, widget=forms.Textarea)
	class Meta:
		model = News
		fields = ['news_title', 'news_desc']
		widgets = {
			'news_desc': Textarea()
		}