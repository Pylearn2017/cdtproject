from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    instrument_purchase = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return '%s' %(self.id)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

'''
from django.db import models
from django.contrib.auth.models import User
from django import forms

class Auth(models.Model):
	user_id = models.IntegerField()
	email = models.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User

class Profile(models.Model):
	#user = models.OneToOneField(User, on_delete=models.PROTECT)
	#avatar = models.ImageField(upload_to = 'avatars/', null = True, blank = True, default = 'avatars/empty_avatar.jpg')
	name = models.CharField(max_length = 30, null = True, blank = True)
	surname = models.CharField(max_length = 30, null = True, blank = True)
	displayed_name = models.CharField(max_length = 48, null = True, blank = True)
	email = models.EmailField(null = True, blank = True)
	#phone = models.PhoneNumberField(null=False, blank=False,)
	phone = models.CharField(max_length = 10, null = True, blank = True)
	password = models.CharField(max_length = 30, null = True, blank = True)
'''