from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from smart_selects.db_fields import ChainedForeignKey

class State(models.Model):
    state = models.CharField(verbose_name='states', max_length=20)
    
    def __str__(self) -> str:
        return self.state
    class Meta:
        ordering = ['id']

# Create your models here.
class Region(models.Model):
    state = models.ForeignKey('State', on_delete=models.CASCADE, related_name="region_state", null=False)
    region = models.CharField(verbose_name='regions', max_length=32)
    
    def __str__(self) -> str:
        return self.region
    
    class Meta:
        ordering = ['id']

class Participant(models.Model):
    GENDER_CHOICES =(
        ('', 'Select gender'),
        ("M", "Male"),
        ("F", "Female")
    )
    
    AGE_CHOICES = (
        ('', 'Select age group'),
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
    
    DENOMINATION_CHOICES = (
        ('', 'Select denomination'),
        ('DLBC', 'Deeper Life Bible Church'),
        ('RCCG', 'The Redeemed Christian Church Of God'),
        ('CAC', 'Christ Apostolic Church'),
        ('AFC', 'Apostolic Faith Church'),
        ('MFM', 'Mountain of Fire and Miracle Ministry'),
        ('GOFAMINT', 'Gospel Faith Mission'),
        ('LFC', 'Living Faith Church'),
        ('CATH', 'Catholic Church'),
        ('ANG', 'Anglican Church'),
        ('BAP', 'Baptist Church'),
        ('CEM', 'Christ Embassy'),
        ('MTH', 'Methodist Church'),
        ('TLC', 'The Lord\'s Chosen'),
        ('CCC', 'Celestial Church of Christ'),
        ('C&S', 'Cherubim and Seraphim'),
        ('OTH', 'Others'),
    )
    
    CATEGORY_CHOICES =(
        ('', 'Select category'),
        ('ENT', 'Enterprenuer'),
        ('UNGRAD', 'Undergraduate'),
        ('GRAD', 'Graduate'),
        ('CORP', 'Corper'),
        ('PRIVATE/GOVR', 'Private/Goverment Worker'),
        ('YOUNG PROF', 'Young Professionals'),
        ('RES', 'Researcher'),
        ('TERT STAFF', 'Tertiary Institution Worker'),
        ('POST SEC', 'Post Secondary School Student'),
        ('OTH', 'Others'),
    )
    
     
    first_name = models.CharField(verbose_name='First name' ,max_length=32)
    last_name = models.CharField(verbose_name='Last name' ,max_length=32)
    gender = models.CharField(verbose_name='Gender', max_length=1, choices=GENDER_CHOICES)
    age = models.CharField(verbose_name='Age', max_length=10, choices=AGE_CHOICES)
    phone_no = PhoneNumberField(unique = True, null=True, blank=True)
    email = models.EmailField(verbose_name='Email', null=True, blank=True, max_length=254)
    linkedin = models.CharField(verbose_name='LinkedIn', null=True, blank=True, max_length=60)
    address = models.CharField(verbose_name='Address', null=True ,max_length=100)
    city = models.CharField(verbose_name='City/Town', null=True, max_length=20)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, related_name='participant_state')
    region = ChainedForeignKey(Region,
                                chained_field="state",
                                chained_model_field="state",
                                show_all=False,
                                auto_choose=True,
                                sort=True)
    category  = models.CharField(verbose_name='Category', null=True, max_length=20, choices=CATEGORY_CHOICES)
    school = models.CharField(verbose_name='School/Work Address', null=True, max_length=100)
    denomination = models.CharField(verbose_name='Denomination', null=True, max_length=10, choices=DENOMINATION_CHOICES)
    registered_date = models.DateTimeField(auto_now_add=True)

    
    @property
    def full_name(self):
        return  f'{self.first_name} {self.last_name}'
    
    def __str__(self) -> str:
        return self.full_name   

    class Meta():
        ordering = ['-registered_date']
        verbose_name = 'participant'
        verbose_name_plural = 'participants'
        
        
class Newcomer(models.Model):
    GENDER_CHOICES =(
        ('', 'Select gender'),
        ("M", "Male"),
        ("F", "Female")
    )
    
    AGE_CHOICES = (
        ('', 'Select age group'),
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
    
    DENOMINATION_CHOICES = (
        ('', 'Select denomination'),
        ('DLBC', 'Deeper Life Bible Church'),
        ('RCCG', 'The Redeemed Christian Church Of God'),
        ('CAC', 'Christ Apostolic Church'),
        ('AFC', 'Apostolic Faith Church'),
        ('MFM', 'Mountain of Fire and Miracle Ministry'),
        ('GOFAMINT', 'Gospel Faith Mission'),
        ('LFC', 'Living Faith Church'),
        ('CATH', 'Catholic Church'),
        ('ANG', 'Anglican Church'),
        ('BAP', 'Baptist Church'),
        ('CEM', 'Christ Embassy'),
        ('MTH', 'Methodist Church'),
        ('TLC', 'The Lord\'s Chosen'),
        ('CCC', 'Celestial Church of Christ'),
        ('C&S', 'Cherubim and Seraphim'),
        ('OTH', 'Others'),
    )
    
    CATEGORY_CHOICES =(
        ('', 'Select category'),
        ('ENT', 'Enterprenuer'),
        ('UNGRAD', 'Undergraduate'),
        ('GRAD', 'Graduate'),
        ('CORP', 'Corper'),
        ('PRIVATE/GOVR', 'Private/Goverment Worker'),
        ('YOUNG PROF', 'Young Professionals'),
        ('RES', 'Researcher'),
        ('TERT STAFF', 'Tertiary Institution Worker'),
        ('POST SEC', 'Post Secondary School Student'),
        ('OTH', 'Others'),
    )
    
     
    first_name = models.CharField(verbose_name='First name' ,max_length=32)
    last_name = models.CharField(verbose_name='Last name' ,max_length=32)
    gender = models.CharField(verbose_name='Gender', max_length=1, choices=GENDER_CHOICES)
    age = models.CharField(verbose_name='Age', max_length=10, choices=AGE_CHOICES)
    phone_no = PhoneNumberField(unique = True, null=True, blank=True)
    email = models.EmailField(verbose_name='Email', null=True, blank=True, max_length=254)
    linkedin = models.CharField(verbose_name='LinkedIn', null=True, blank=True, max_length=60)
    address = models.CharField(verbose_name='Address', null=True ,max_length=100)
    city = models.CharField(verbose_name='City/Town', null=True, max_length=20)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, related_name='newcomer_state')
    region = ChainedForeignKey(Region,
                                chained_field="state",
                                chained_model_field="state",
                                show_all=False,
                                auto_choose=True,
                                sort=True)
    category  = models.CharField(verbose_name='Category', null=True, max_length=20, choices=CATEGORY_CHOICES)
    school = models.CharField(verbose_name='School/Work Address', null=True, max_length=100)
    denomination = models.CharField(verbose_name='Denomination', null=True, max_length=10, choices=DENOMINATION_CHOICES)
    registered_date = models.DateTimeField(auto_now_add=True)

    
    @property
    def full_name(self):
        return  f'{self.first_name} {self.last_name}'
    
    def __str__(self) -> str:
        return self.full_name   
    class Meta:
        ordering = ['-registered_date']
        verbose_name = 'newcomer'
        verbose_name_plural = 'newcomers'


class Convert(models.Model):
    GENDER_CHOICES =(
        ('', 'Select gender'),
        ("M", "Male"),
        ("F", "Female")
    )
    
    AGE_CHOICES = (
        ('', 'Select age group'),
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
    
    DENOMINATION_CHOICES = (
        ('', 'Select denomination'),
        ('DLBC', 'Deeper Life Bible Church'),
        ('RCCG', 'The Redeemed Christian Church Of God'),
        ('CAC', 'Christ Apostolic Church'),
        ('AFC', 'Apostolic Faith Church'),
        ('MFM', 'Mountain of Fire and Miracle Ministry'),
        ('GOFAMINT', 'Gospel Faith Mission'),
        ('LFC', 'Living Faith Church'),
        ('CATH', 'Catholic Church'),
        ('ANG', 'Anglican Church'),
        ('BAP', 'Baptist Church'),
        ('CEM', 'Christ Embassy'),
        ('MTH', 'Methodist Church'),
        ('TLC', 'The Lord\'s Chosen'),
        ('CCC', 'Celestial Church of Christ'),
        ('C&S', 'Cherubim and Seraphim'),
        ('OTH', 'Others'),
    )
    
    CATEGORY_CHOICES =(
        ('', 'Select category'),
        ('ENT', 'Enterprenuer'),
        ('UNGRAD', 'Undergraduate'),
        ('GRAD', 'Graduate'),
        ('CORP', 'Corper'),
        ('PRIVATE/GOVR', 'Private/Goverment Worker'),
        ('YOUNG PROF', 'Young Professionals'),
        ('RES', 'Researcher'),
        ('TERT STAFF', 'Tertiary Institution Worker'),
        ('POST SEC', 'Post Secondary School Student'),
        ('OTH', 'Others'),
    )
         
    first_name = models.CharField(verbose_name='First name' ,max_length=32)
    last_name = models.CharField(verbose_name='Last name' ,max_length=32)
    gender = models.CharField(verbose_name='Gender',max_length=1, choices=GENDER_CHOICES)
    age = models.CharField(verbose_name='Age', max_length=10, choices=AGE_CHOICES)
    phone_no = PhoneNumberField(unique = True, null=True, blank=True)
    email = models.EmailField(verbose_name='Email', null=True, blank=True, max_length=254)
    linkedin = models.CharField(verbose_name='LinkedIn', null=True, blank=True, max_length=60)
    address = models.CharField(verbose_name='Address', max_length=100)
    city = models.CharField(verbose_name='City/Town', max_length=20)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, related_name='convert_state')
    region = ChainedForeignKey(Region,
                                chained_field="state",
                                chained_model_field="state",
                                show_all=False,
                                auto_choose=True,
                                sort=True)
    category  = models.CharField(verbose_name='Category', null=True, max_length=20, choices=CATEGORY_CHOICES)
    school = models.CharField(verbose_name='School/Work Address', null=True, max_length=100)
    denomination = models.CharField(verbose_name='Denomination', null=True, max_length=10, choices=DENOMINATION_CHOICES)
    registered_date = models.DateTimeField(auto_now_add=True)

    
    @property
    def full_name(self):
        return  f'{self.first_name} {self.last_name}'
    
    def __str__(self) -> str:
        return self.full_name
    
    class Meta():
        ordering = ['-registered_date']
        verbose_name = 'convert'
        verbose_name_plural = 'converts'