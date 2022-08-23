from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


""" Custom User Start """
# class CustomUser(AbstractUser):
#     user_type_choices=(
#         (1, 'Admin'),
#         (2, 'Staff'),
#         (2, 'Merchant'),
#         (4, 'Customer'))
#     user_type=models.CharField(   
#         max_length=256, 
#         choices=user_type_choices,
#         default=1)
""" Custom User End """   

""" Users Types """
# class AdminUser(models.Model):
#     profile_picture=models.FileField(default='')
#     auth_user_id=models.OneToOneField(
#         CustomUser,
#         on_delete=models.CASCADE
#     )
#     created_at=models.DateTimeField(auto_now_add=True)

# class StaffUser(models.Model):
#     profile_picture=models.FileField(default='')
#     auth_user_id=models.OneToOneField(
#         CustomUser,
#         on_delete=models.CASCADE
#     )
#     created_at=models.DateTimeField(auto_now_add=True)

# class MerchantUser(models.Model):
#     profile_picture=models.FileField(default='')
#     auth_user_id=models.OneToOneField(
#         CustomUser,
#         on_delete=models.CASCADE
#     )
#     company_name=models.CharField(max_length=256)
#     gst_details=models.CharField(max_length=256)
#     address=models.TextField()
#     created_at=models.DateTimeField(auto_now_add=True)

# class CustomerUser(models.Model):
#   profile_picture=models.FileField(default='')
#   auth_user_id=models.OneToOneField(
#   CustomUser,
#   on_delete=models.CASCADE)
# created_at=models.DateTimeField(auto_now_add=True)
""" Users Types """

""" Categories and Sub Categories """
# Categories Model
class Categories(models.Model):
    id=models.AutoField(
        primary_key=True
    )
    name=models.CharField(
        max_length =128
    )
    slug=models.SlugField(
        blank=True,
        null=True 
    )
    description=models.TextField(
        max_length=512
    )
    thumbnail=models.FileField(
        blank=True
    )
    is_active=models.IntegerField(
        default=1
    )
    created_at=models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
    
    def save(self, *arg, **kwarg):
        if self.slug is None:
            self.slug=slugify(self.name)
        super().save(*arg, **kwarg)

# Sub Categories Model
class SubCategories(models.Model):
    id=models.AutoField(
        primary_key=True)
    category_id=models.ForeignKey(
        Categories, 
        on_delete=models.SET_NULL, 
        null=True
    )
    name=models.CharField(
        max_length=128
    )
    slug=models.SlugField(
        blank=True,
        null=True 
    )
    description=models.TextField(
        max_length=512,
        null=True)
    thumbnail=models.FileField(
        blank=True

    )
    pub_date=models.DateField(
        'date published', 
        blank= True, 
        null=True)
    is_active=models.IntegerField(
        default=1
    )
    created_at=models.DateTimeField(
        auto_now_add=True,
        blank= True, 
        null=True)

    def __str__(self):
        return self.name

    def save(self, *arg, **kwarg):
        if self.slug is None:
            self.slug=slugify(self.name)
        super().save(*arg, **kwarg)

""" Categories and Sub Categories """

""" Dropdown Tables Starts """
# Titles Model
class Title(models.Model):
    id=models.AutoField(
        primary_key=True)
    name=models.CharField(
        max_length=128)
    description=models.CharField(
        max_length=128)
    
    def __str__(self):
        return self.name

# Gender Model
class Gender(models.Model):
    id=models.AutoField(
        primary_key=True)
    name=models.CharField(
        max_length=16)
    
    def __str__(self):
        return self.name

# Marital Status Model
class MaritalStatus(models.Model):
    id=models.AutoField(
        primary_key=True)
    name=models.CharField(
        max_length=16)
    
    def __str__(self):
        return self.name

class Region(models.Model):
    id=models.AutoField(
        primary_key=True)
    name=models.CharField(
        max_length =128)
    
    def __str__(self):
        return self.name

class TownCity(models.Model):
    id=models.AutoField(
        primary_key=True)
    name=models.CharField(
        max_length =128)
    region=models.ForeignKey(
        Region,
        on_delete=models.SET_NULL,
        null=True)
    
    def __str__(self):
        return self.name

class Office(models.Model):
    id=models.AutoField(
        primary_key=True)
    name=models.CharField(
        max_length =128)
    town_city=models.ForeignKey(
        TownCity,
        on_delete=models.SET_NULL,
        null=True)
    
    def __str__(self):
        return self.name

""" Dropdown Tables Ends """

""" Personal Information Starts """
# Person Model
class Person(models.Model):
    id=models.AutoField(
        primary_key=True)
    title=models.ForeignKey(
        Title, 
        on_delete=models.SET_NULL, 
        null=True)
    surName=models.CharField(
        max_length =128, 
        null=True)
    lastName=models.CharField(
        max_length =128, 
        null=True)
    otherName=models.CharField(
        max_length =128, 
        null=False, 
        blank=True)
    description=models.TextField(
        max_length=512, 
        blank=False)

    dateOfBirth=models.DateField(
        'date of Birth', 
        blank=True, 
        null=True)
    gender=models.ForeignKey(
        Gender, 
        on_delete=models.SET_NULL, 
        null=True)
    maritalStatus=models.ForeignKey(
        MaritalStatus, 
        on_delete=models.SET_NULL, 
        null=True)

    mobile_1=models.CharField(
        max_length= 14, 
        blank=True )
    mobile_2=models.CharField(
        max_length= 14, 
        blank=True )
    email1=models.EmailField(
        max_length= 64, 
        blank=True )
    email2=models.EmailField(
        max_length= 64, 
        blank=True )
    
    def __str__(self):
        return self.description
""" Personal Information Ends """

# Positions Lookups
class Position(models.Model):
    id=models.AutoField(
        primary_key=True)
    name=models.CharField(
        max_length=64)
    description=models.TextField(
        max_length=512, 
        blank=False,
        default='type something here')

    def __str__(self):
        return self.name

class Profession(models.Model):
    id=models.AutoField(
        primary_key=True)
    name=models.CharField(
        max_length=64)
    description=models.TextField(
        max_length=512, 
        blank=False,
        default='type something here')

    def __str__(self):
        return self.name

class Rank(models.Model):
    id=models.AutoField(
        primary_key=True)
    name=models.CharField(
        max_length=64)
    description=models.TextField(
        max_length=512, 
        blank=False,
        default='type something here')

    def __str__(self):
        return self.name

class Department(models.Model):
    id=models.AutoField(
        primary_key=True)
    name=models.CharField(
        max_length =128
    )

    def __str__(self):
        return self.name

# Staff Model
class Staff(models.Model):
    id=models.AutoField(primary_key=True)

    staff_number=models.CharField(
        max_length=32,
        default='QW23')

    person_id=models.ForeignKey(
        Person, 
        on_delete=models.SET_NULL, 
        null=True)
    
    department_id=models.ForeignKey(
        Department, 
        on_delete=models.SET_NULL, 
        null=True)
    
    position_id=models.ForeignKey(
        Position, 
        on_delete=models.SET_NULL, 
        null=True)

    profession_id=models.ForeignKey(
        Profession, 
        on_delete=models.SET_NULL, 
        null=True)

    rank_id=models.ForeignKey(
        Rank, 
        on_delete=models.SET_NULL, 
        null=True)

    office_id=models.ForeignKey(
        Office, 
        on_delete=models.SET_NULL, 
        null=True)

    description=models.TextField(
        max_length=512)

    dateOfFirstAppointment=models.DateField(
        'date of First Appointment', 
        blank= True, 
        null=True)
   
    def __str__(self):
        return self.description

# Directors Model
class BoardOfDirectors(models.Model):
    id=models.AutoField(
        primary_key=True)
    person=models.ForeignKey(
        Person, 
        on_delete=models.SET_NULL, 
        null=True)
    position=models.ForeignKey(
        Position, 
        on_delete=models.SET_NULL, 
        null=True)
    description=models.TextField(
        max_length=512)
    dateOfFirstAppointment=models.DateField(
        'date of First Appointment',
        null=True, 
        blank=True)
   
    def __str__(self):
        return self.description

# Management Model
class Management(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(
        Staff, 
        on_delete=models.SET_NULL, 
        null=True)
    position_id=models.ForeignKey(
        Position, 
        on_delete=models.SET_NULL, 
        null=True)
    description=models.TextField(
        max_length=512)
    dateOfFirstAppointment=models.DateField(
        'date of First Appointment', 
        blank= True, 
        null=True)
   
    def __str__(self):
        return self.description

""" Projects Information Starts """

# Projects Model
class Project(models.Model): 
    id=models.AutoField(primary_key=True)
    sub_category=models.ForeignKey(
        SubCategories, 
        on_delete=models.SET_NULL, 
        null=True)
    name=models.CharField(
        max_length =256)
    slug=models.SlugField(
        blank=True,
        null=True)
    description=models.TextField(
        )
    location= models.CharField(
        max_length=128, 
        null=True)
    cost=models.CharField(
        max_length=128, 
        null=True,
        default='') 
    client=models.CharField(
        max_length=128, 
        null=True)
    total_floor_area=models.CharField(
        max_length=128, 
        null=True)
    coordinator=models.ForeignKey(
        Staff,
        on_delete=models.SET_NULL,
        null=True)
    jobsheet=models.FileField( 
        null=True)
    start_date=models.DateField(
        blank=True, 
        null=True,
        auto_now_add=True)
    completed_date=models.DateField(
        blank=True, 
        null=True,
        auto_now=True)   

    def __str__(self):
        return self.name

    def save(self, *arg, **kwarg):
        if self.slug is None:
            self.slug=slugify(self.name)
        super().save(*arg, **kwarg) 

class ProjectLead(models.Model):
    id=models.AutoField(primary_key=True)
    project_id=models.ForeignKey(
        Project, on_delete=models.SET_NULL,
        null=True)
    staff_id=models.ForeignKey(
        Staff, on_delete=models.SET_NULL,
        null=True)

    description = models.CharField(
        max_length=128, 
        null=True)
        
    def __str__(self):
        return self.description
        
    def save(self, *arg, **kwarg):
        if self.slug is None:
            self.slug=slugify(self.description)
        super().save(*arg, **kwarg) 

class ProjectDetail(models.Model):
    id=models.AutoField(primary_key=True)
    project_id=models.ForeignKey(
        Project, on_delete=models.SET_NULL,
        null=True
    )
    title=models.CharField(
        max_length=256)
    title_details=models.CharField(
        max_length=256
    )
    created_date=models.DateField(
        blank=True, 
        null=True,
        auto_now=True)

class ProjectMedia(models.Model):
    id=models.AutoField(primary_key=True)
    project_id=models.ForeignKey(
        Project, 
        on_delete=models.CASCADE,
        null=True
    )
    media_type_choice = (
        (1, 'Image'),
        (2,'Video'),
        )
    media_type = models.CharField(
        max_length=256,
    )
    media_content = models.FileField(
    )

class ProjectOverview(models.Model):
    id=models.AutoField(primary_key=True)
    project_id=models.ForeignKey(
        Project, on_delete=models.SET_NULL,
        null=True
    )
    title=models.CharField(
        max_length=256)
    created_at=models.DateTimeField(
        auto_now_add=True)
    
class ProjectTag(models.Model):
    id=models.AutoField(primary_key=True)
    project_id=models.ForeignKey(
        Project, 
        on_delete=models.SET_NULL,
        null=True
    )
    title=models.CharField(
        max_length=256)
    created_at=models.DateTimeField(
        auto_now_add=True)
 
""" Projects Information Ends """

""" Recievers Start """
# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.user_type == 1:
#             AdminUser.objects.create(
#                 auth_user_id=instance)

#         if instance.user_type == 2:
#             StaffUser.objects.create(
#                 auth_user_id=instance)

#         if instance.user_type == 3:
#             MerchantUser.objects.create(
#                 auth_user_id=instance,
#                 company_name='', 
#                 gst_details='',
#                 address='')

#         if instance.user_type == 4:
#             CustomerUser.objects.create(
#                 auth_user_id=instance)

# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs): 
#     if instance.user_type == 1:
#         instance.adminuser.save()
#     if instance.user_type == 2:
#         instance.staffuser.save()
#     if instance.user_type == 3:
#         instance.merchantuser.save()
#     if instance.user_type == 4:
#         instance.customeruser.save()
""" Recievers End """