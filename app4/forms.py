from django.core import validators
from django import forms 
from .models import Job_Openings
class Job_Openings_Registration(forms.ModelForm):
    
    class Meta:
        model = Job_Openings
        fields =["job_title","job_type","qualification",
              "skill_sets","certifications","annualsalary_lacs",
              "annualsalary_thousands","other_remark","locations",
              "college_preference","joining_priod","experience_year",
              "experience_months","NoOf_Vacancy","job_description",
              "job_responsibilty"]
