from django import forms
from django.contrib.auth.forms import AuthenticationForm
# from tensorboard import program
from .models import Location, Participant, Convert
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class AuthForm(AuthenticationForm):
    username = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ('username', 'password')
    

class LocationForm(forms.ModelForm):
    region = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Region'}))
    group = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Group'}))
    district = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'District'}))
    
    class Meta:
        model = Location
        fields = ('region', 'group', 'district')
        

class ParticipantForm(forms.ModelForm):
    GENDER_CHOICES =(
        ("M", "Male"),
        ("F", "Female")
    )
    
    AGE_CHOICES = (
        ('16-20', '16-20'),
        ('21-25', '21-25'),
        ('26-30', '26-30'),
        ('30-35', '30-35'),
        ('36-40', '36-40'),
        ('41-45', '41-45'),
        ('46-50', '46-50'),
        ('51-55', '51-55'),
        ('56-60', '56-60'),
        ('Above 60', 'Above 60'),
    )
        
    first_name = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    gender = forms.ChoiceField(label="Select gender", choices=GENDER_CHOICES, required=True, widget=forms.Select())
    age = forms.ChoiceField(choices=AGE_CHOICES, required=True, widget=forms.Select())
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone_no = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial="NG"))
    linkedin = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'placeholder': 'LinkedIn'}))
    address = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    town = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':'Town'}))
    state = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'State'}))
    school = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'School'}))
    profession = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Profession'}))
    denomination = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Denomination'}))
    # program = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model = Participant
        fields = ('first_name', 'last_name', 'gender', 'age', 'email', 'phone_no', 'linkedin', 'address', 'town', 'state',
                  'school', 'profession', 'member', 'denomination')
        
class ConvertForm(forms.ModelForm):
    GENDER_CHOICES =(
        ("M", "Male"),
        ("F", "Female")
    )
    
    AGE_CHOICES = (
        ('16-20', '16-20'),
        ('21-25', '21-25'),
        ('26-30', '26-30'),
        ('30-35', '30-35'),
        ('36-40', '36-40'),
        ('41-45', '41-45'),
        ('46-50', '46-50'),
        ('51-55', '51-55'),
        ('56-60', '56-60'),
        ('Above 60', 'Above 60'),
    )
    first_name = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, widget=forms.Select())
    age = forms.ChoiceField(choices=AGE_CHOICES, required=True, widget=forms.Select())
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone_no = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial="NG"))
    address = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    town = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':'Town'}))
    state = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'State'}))
    school = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'School'}))
    profession = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Profession'}))
    # program = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model = Convert
        # widgets = {
        #     'phone_no': PhoneNumberPrefixWidget(initial="NG")
        # }
        fields = ('first_name', 'last_name', 'gender', 'age', 'email', 'phone_no', 'address', 'town', 'state',
                  'school', 'profession')