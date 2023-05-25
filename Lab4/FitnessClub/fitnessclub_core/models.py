from django.db import models


class Client(models.Model):
    email = models.EmailField(max_length=50, unique=True, help_text='Enter email address')
    first_name = models.CharField(max_length=30, help_text='Enter first name')
    last_name = models.CharField(max_length=30, help_text='Enter last name')
    phone_number = models.CharField(max_length=20, help_text='Enter phone number')

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, help_text='Enter first name')
    last_name = models.CharField(max_length=30, help_text='Enter last name')
    price_per_hour = models.IntegerField(max_length=3, help_text='Pprice per hour of training')
    specialization = models.TextField(max_length=150, help_text='Info about treiner specialization')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

class Gym(models.Model):
    name = models.CharField(max_length=20, help_text='Name of the gym')
    open_time = models.TimeField(auto_now=False, auto_now_add=False, help_text='Gym opening time')
    close_time = models.TimeField(auto_now=False, auto_now_add=False, help_text='Gym closing time')
    address = models.CharField(max_length=30, help_text='Address of the gym')

    def __str__(self) -> str:
        return f'{self.name}'
    

class Gym_membership(models.Model):
    name = models.CharField(max_length=20, help_text='Name of gym membership')
    description = models.TextField(max_length=200, help_text='Description of gym membership')
    cost = models.IntegerField(max_length=4, help_text='Cost of the gym membership')

    def __str__(self) -> str:
        return f'{self.name}'
    