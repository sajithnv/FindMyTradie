from django.db import models

# Create your models here.
LOCATIONS=(
	('0','Kanhangad'),
	('1','Kasaragod'),
	('2','Kenjar'),
	('3','Bajpe'),
	('4','Mangalore'),
	('5','Payyanoor'),
    ('6','Sulliya'),
    ('7','Kannur'),
    ('8','Kozhikode'),
    ('9','Kollam'),
    ('10','Kottayam'),
    ('11','Thiruvanathapuram'),
	)
TRADES=(
    ('0','Plumber'),
    ('1','Painter'),
    ('2','Electrician'),
    ('3','Carpender'),
    ('4','Welder'),
    ('5','TV Technician'),
    ('6','Refrigerator Technician'),
    ('7','Motor Technician'),
    ('8','Coconut Climber'),
    ('9','Gardener'),
)
FEEDBACK=(
    ('0','Idle'),
    ('1','Positive'),
    ('2','Negative'),
)
class user_register(models.Model):
    u_name=models.CharField('User_Name',max_length=100,null=True,unique=True)
    phone_number=models.CharField('Phone_Number',max_length=10,primary_key=True)
    whatsapp_number=models.CharField('Whatsapp_Number',max_length=10)
    address=models.CharField('Address',max_length=100)
    date=models.DateTimeField(auto_now_add=True)
class emp_register(models.Model):
    e_name=models.CharField('Employee_Name',max_length=100,unique=True)
    phone_number=models.CharField('Phone_Number',max_length=10,primary_key=True)
    e_img=models.ImageField('Employee Image',upload_to='.\static\img\emp_img')
    address=models.CharField('Address',max_length=100)
    location=models.CharField('Location',choices=LOCATIONS,default='1',max_length=20)
    service_name=models.CharField('Trade Name',choices=TRADES,max_length=30)
    certificate_img=models.ImageField('Trade Proof',upload_to='.\static\img\certificate_img')
    available=models.BooleanField(default=True)
    verified=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)

class services(models.Model):
    u_name=models.CharField(max_length=100)
    e_name=models.CharField(max_length=100)
    service_name=models.CharField('Trade Name',max_length=30)
    date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateTimeField(null=True)
    requested=models.BooleanField(default=False)
    paid=models.BooleanField(default=False)
    accepted=models.BooleanField(default=False)
    rejected=models.BooleanField(default=False)
    working=models.BooleanField(default=False)
    confirm_working=models.BooleanField(default=False)
    completed=models.BooleanField(default=False)
    cancelled=models.BooleanField(default=False)
    feedback=models.BooleanField(null=True)