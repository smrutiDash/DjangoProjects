from django.contrib import admin
from .models import Job_Openings,Apply_job
class Job_OpeningsAdmin(admin.ModelAdmin):

   list_display= ('job_title','job_type','qualification','skill_sets','certifications',
    'annualsalary_lacs','annualsalary_thousands','other_remark',
    'locations','college_preference','joining_priod','experience_year',
    'experience_months','NoOf_Vacancy','job_description','job_responsibilty')
   radio_fields = {'job_type': admin.VERTICAL,
                   'joining_priod': admin.VERTICAL,
                   }

admin.site.register(Job_Openings,Job_OpeningsAdmin)
admin.site.register(Apply_job)

