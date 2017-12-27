from django.forms import ModelForm
from .models import Professor
from sessionManagerApp.models import Course

class AddProfessorForm(ModelForm):
	# professor_name = forms.CharField(max_length=100, label='Name')
	# professor_info = forms.CharField(max_length=1000, label='Information', widget=forms.Textarea)
	# professor_image = forms.ImageField(null=True, blank=True)
	class Meta:
		model = Professor
		fields = ['name', 'info', 'image']

class AddCourseForm(ModelForm):
	class Meta:
		model = Course
		fields = ['name', 'info', 'prequels']