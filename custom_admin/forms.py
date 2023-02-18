from django import forms
from .models import Participant, Convert, Newcomer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class MainForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['linkedin'].required = False
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('gender', css_class='form-group col-md-6 mb-0'),
                Column('age', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('phone_no', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('linkedin', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('address', css_class='form-group col-md-9 mb-0'),
                Column('city', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('state', css_class='form-group col-md-6 mb-0'),
                Column('region', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'category',
            'school',
            'denomination',

            Submit('submit', 'Register Participant')
        )
    

class ParticipantForm(MainForm):
    class Meta:
        model = Participant
        fields = '__all__'


class ConvertForm(MainForm):

    class Meta:
        model = Convert
        fields = '__all__'
        
       
class NewcomerForm(MainForm):
    class Meta:
        model = Newcomer
        fields = '__all__'