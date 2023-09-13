from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User




# Create your models here.
# class Employer(models.Model):
#     company=models.CharField(max_length=255)
#     address=models.CharField(max_length=255)
#     contact_person=models.CharField(max_length=255)
#     contact_no=models.CharField(max_length=10)
#     email=models.EmailField()
#     website=models.CharField(max_length=255)

class Company(models.Model):
    company=models.CharField(max_length=255, verbose_name="Company")
    address1=models.CharField(max_length=255, blank=True, verbose_name="Address 1" )
    address2=models.CharField(max_length=255, blank=True, verbose_name="Address 2")
    address3=models.CharField(max_length=255, blank=True, verbose_name="Address 3")
    phone=models.CharField(max_length=10, verbose_name="Phone")
    email=models.EmailField(blank=True, verbose_name="Email")
    website=models.CharField(max_length=255, blank=True, verbose_name="Website")
    logo=models.ImageField(upload_to='logo', verbose_name="Logo")

    class Meta:
        verbose_name_plural="Company"

class Qualification(models.Model):
    qualificationName = models.CharField(max_length=255, verbose_name="Qualification Name")

    class Meta:
        verbose_name_plural="Qualification"

class State(models.Model):
    statename=models.CharField(max_length=255, verbose_name="State Name")
    def __str__(self):
        return self.statename
    
    class Meta:
        verbose_name_plural="State"
    
    
    

class District(models.Model):
    state =models.ForeignKey(State, on_delete=models.CASCADE, verbose_name="State")
    districtname = models.CharField(max_length=255,unique=True, verbose_name="District Name")
    def __str__(self):
        return self.districtname
    
    class Meta:
        verbose_name_plural="District"

   

# class Syllabus(models.Model):
#     Syllabus_name =models.CharField(max_length=255)

# class CourseName(models.Model):
#     course_name =models.CharField(max_length=255)

class Branch(models.Model):
    branch_name = models.CharField(max_length=255, verbose_name="Branch Name")
    branch_code = models.CharField(max_length=255, verbose_name="Branch Code")
    address = models.CharField(max_length=255, blank=True, verbose_name="Adress")
    street = models.CharField(max_length=255, blank=True, verbose_name="Street")
    state =models.ForeignKey(State, on_delete=models.CASCADE, verbose_name="State")
    district =ChainedForeignKey(District,chained_field="state",chained_model_field="state",show_all=False,auto_choose=True,sort=True, verbose_name="District")
    pincode =models.CharField(max_length=6, blank=True, verbose_name="Pincode")
    mobile_number =models.CharField(max_length=10, verbose_name="Mobile Number")
    email = models.EmailField(verbose_name="Email")

    

    class Meta:
        verbose_name_plural="Branch"

    

# class Batches(models.Model):
#     course =models.CharField(max_length=255, verbose_name="Cource")
#     trainer =models.CharField(max_length=255, verbose_name="Trainer")   
#     state_date =models.DateTimeField(null=True, verbose_name="Starte Date")
#     end_date =models.DateField(null=True, verbose_name="End Date")

#     class Meta:
#         verbose_name_plural="Batches"
    
        

    

class EnquirySource(models.Model):
    enquirysourcename=models.CharField(max_length=255, verbose_name="Enquiry Source Name")
    def __str__(self):
        return self.enquirysourcename

    class Meta:
        verbose_name_plural="Enquiry Source"

# class Cource(models.Model):
#     cource_name =models.CharField(max_length=255, verbose_name="Course:")
#     cource_code =models.CharField(max_length=20, verbose_name="Cource Code:")
#     trainers = models.ManyToManyField(User, related_name="Trainer", blank=True, limit_choices_to={'is_active': True, 'groups__name': 'Faculty'})
    
#     def __str__(self):
#         return self.cource_name
    
#     class Meta:
#         verbose_name_plural="Cource"


class MasterData(models.Model):
    name =models.CharField(max_length=255, verbose_name="Name")
    value =models.CharField(max_length=255, verbose_name="Value")
    type =models.CharField(max_length=255, verbose_name="Type")  

    class Meta:
        verbose_name_plural="Master Data"



class Followupstatusname(models.Model):
    Followupstatusname=models.CharField(max_length=255, verbose_name="Folloup Status Name")
    bool_value=((True,'Yes'),(False,'No'))
    Followupstatus=models.BooleanField(choices=bool_value, verbose_name="Followup Status")

    def __str__(self):
        return self.Followupstatusname

    class Meta:
        verbose_name_plural="Followup status name"

class Course(models.Model):
    course = models.CharField(max_length=200, unique=True)
    coursecode = models.CharField(max_length=200, unique=True, null=True)
    trainers = models.ManyToManyField(
                                      User, 
                                      related_name="trainers",
                                      blank=True,
                                      limit_choices_to={"is_active":True,"groups__name": 'Faculty'}
                                      )
    is_active = models.BooleanField()
    

    class Meta:
        verbose_name_plural = "Course"
    def __str__(self):
        return self.course

class Batch(models.Model):
    batch = models.CharField(max_length=200, unique=True)
    course =models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name="Course:",null=True,blank=False,limit_choices_to={"is_active": True})
    trainer =models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Trainer",null=True, blank=False,related_name="trainer",limit_choices_to={"is_active": True, "groups__name": 'Faculty'})
    # trainer =ChainedForeignKey(User,chained_field='course',chained_model_field='Faculty',related_name='user_group',show_all=False,auto_choose=True,sort=True,on_delete=models.CASCADE,verbose_name="Trainer",null=True, blank=False,limit_choices_to={"is_active": True, "groups__name": 'Faculty'})
  
    start_date =models.DateTimeField(null=True, verbose_name="Start Date")
    end_date =models.DateField(null=True, verbose_name="End Date")

    



