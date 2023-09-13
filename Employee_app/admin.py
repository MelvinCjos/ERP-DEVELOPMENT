from django.contrib import admin
from .models import Company,State,District,Qualification,Branch,EnquirySource,Course,Followupstatusname,MasterData,Batch
from .forms import BachForm 
from django.contrib.admin import AdminSite


# class PlacementAdminSite(AdminSite):

    # def get_app_list(self, app, request):
    #     #print("hiapp")
    #     #pass

    # def get_app_list(self, request):
    #     #print("hi")
    #     """
    #     Return a sorted list of all the installed apps that have been
    #     registered in this site.
    #     """
    #     ordering = {
    #         "Company": 1,
    #         "State": 2,
    #         "District": 3,
    #         "Branch": 4,
    #         "Enquiry Source": 5,
    #         "Followup status name": 6,
    #         "Qualification": 7,
    #         "Batches": 8,
    #         "Cource": 9,
    #         "Master Data":10}
        
    #     app_dict = self._build_app_dict(request)

    #     app_list = list(app_dict.values())
    #     # app_list.sort(key=lambda x: appordering[x['name']])

    #     for app in app_list:
    #         app['models'].sort(key=lambda x: ordering[x['name']])

    #         return app_list

# mysite = PlacementAdminSite()
# admin.site = mysite    


class BatchAdmin(admin.ModelAdmin):
    list_display=('course','trainer','start_date','end_date')
    form=BachForm


class CourseAdmin(admin.ModelAdmin):
    filter_horizontal=('trainers',)           
        

admin.site.register(District, order=1)
admin.site.register(State)
admin.site.register(Qualification)
admin.site.register(Branch)
admin.site.register(Batch,BatchAdmin)
admin.site.register(EnquirySource)
admin.site.register(Company)
admin.site.register(Course,CourseAdmin)
admin.site.register(Followupstatusname)
admin.site.register(MasterData)



