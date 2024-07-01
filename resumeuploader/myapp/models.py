from django.db import models

# Create your models here.
STATE_CHOICE = (('Andhra Pradesh', 'Andhra Pradesh'),
                ('Arunachal Pradesh', 'Arunachal Pradesh') ,
                ('Assam', 'Assam'),
                ('Bihar', 'Bihar'),
                ('Chhattisgarh', 'Chhattisgarh'),
                ('Goa', 'Goa'),
                ('Gujarat', 'Gujarat'),
                ('Haryana', 'Haryana'),
                ('Himachal Pradesh', 'Himachal Pradesh'),
                ('Jammu and Kashmir', 'Jammu and Kashmir'),
                ('Jharkhand', 'Jharkhand'),
                ('Karnataka', 'Karnataka'),
                ('Kerala', 'Kerala'),
                ('Madhya Pradesh', 'Madhya Pradesh'),
                ('Maharashtra', 'Maharashtra')

                ) 
             
 
# 
# Manipur
# Meghalaya
# Mizoram
# Nagaland
# Odisha
# Punjab
# Rajasthan
# Sikkim
# Tamil Nadu
# Telangana
# Tripura
# Uttar Pradesh
# Uttarakhand
# West Bengal
# Andaman and Nicobar Islands
# Chandigarh
# Dadra and Nagar Haveli
# Daman and Diu
# Lakshadweep
# National Capital Territory of Delhi
# Puducherry)

class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=50)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices= STATE_CHOICE, max_length=100)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profileImg', blank= True)
    my_file = models.FileField(upload_to='doc', blank=True)