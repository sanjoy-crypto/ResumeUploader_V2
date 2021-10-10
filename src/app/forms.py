from django import forms
from .models import Resume

GENDER = [
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
]
JOB_CITY = (
    ('Dhaka', 'Dhaka'),
    ('Gazipur', 'Gazipur'),
    ('Chittagong', 'Chittagong'),
    ('Khulna', 'Khulna'),
    ('Sylhet', 'Sylhet'),
    ('Rajshahi', 'Rajshahi'),
    ('Mymensingh', 'Mymensingh'),
    ('Barisal', 'Barisal'),
    ('Rangpur', 'Rangpur'),
    ('Comilla', 'Comilla'),
    ('Narayanganj', '	Narayanganj'),
    )

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER,widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(choices=JOB_CITY,widget=forms.CheckboxSelectMultiple,label='Preferred Job Locations')
    class Meta:
        model = Resume
        fields = ['name','birth','gender','work','education','phone','email','experience','locality','city','zip','job_city','profile_image','my_file']

        labels = {'name':'Full Name','birth':'Date of Birth','experience':'Job Experience','zip':'Zip Code','profile_image':'Profile Image','my_file':'Document'}

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'birth':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'work':forms.TextInput(attrs={'class':'form-control'}),
            'education':forms.Textarea(attrs={'class':'form-control','rows':'3'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'experience':forms.Textarea(attrs={'class':'form-control','rows':'3'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.Select(attrs={'class':'form-control'}),
            'zip':forms.NumberInput(attrs={'class':'form-control'}),
        }