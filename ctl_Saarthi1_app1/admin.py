from django.contrib import admin
from .models import Add_Member1
from .models import Add_Member2

class Add_Member1Admin(admin.ModelAdmin):

     list_display= ('title','first_name','middle_name',
        'last_name','age','dob','mob_no','address','pin_code',
         'comment','email_id','test','total_amount','overall_discount',
        'gross_amount','discount_amount','net_amount','due_amount',
         'cash_amount','paid_amount','payment_getway','remark'
                           )


class Add_Member2Admin(admin.ModelAdmin):
    list_display = ('id','reg_no','title','first_name','middle_name','last_name','gender','email_id','dob',
 'age','mob_no','address','pin_code','date_Of_Enrollment','blood_group','marital_status','wedding_aniversary_date',
 'house_hold_status','income_level','height','weight','occupation','community','religion','family_relationship')

admin.site.register(Add_Member1,Add_Member1Admin)
admin.site.register(Add_Member2,Add_Member2Admin)