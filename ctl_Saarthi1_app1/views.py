from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import ctl_Saarthi1_app1_loginForm
from django.contrib.auth.models import User, Group

from .models import Add_Member2
from django.http import JsonResponse, HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
import json
from datetime import datetime


def department(request):
    return render(request,'department.html')
def demo(request):
    return render(request,'view-member-detail-copy.html')
def membership(request):
    return render(request,'membership.html')
def signup(request):
    return render(request,'signup.html') 
def forgotpassword(request):
    return render(request,'forgotpassword.html') 


def login(request):
    myapp_fm=ctl_Saarthi1_app1_loginForm()  
    if request.method == "POST":
       
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('department')
        
        else:
            messages.error(request, 'Error! please enter the correct  Username and Password for a staff account.')
            return render(request,'login.html',{'form':myapp_fm})

    else:
        return render(request,"login.html",{'form':myapp_fm})

def add_member(request):
    print("something")
     
    if request.method == "POST":
       print(request.POST)
       #import ipdb;ipdb.set_trace()
       resultData = prepareModelData(request.POST)

       print("inside if --------------")
       title=resultData['title']
       print("request.POST-----------------")
       first_name=resultData['first_name']
       print("first_name----------------")
       middle_name=resultData['middle_name']
       last_name=resultData['last_name']
       gender=resultData['gender']
       email_id=resultData['email_id']
       dob=resultData['dob']
       age=resultData['age']
       mob_no=resultData['mob_no']
       address=resultData['address']
       print("Address-----------------------######")
       pin_code=resultData['pin_code']
       date_Of_Enrollment=resultData['date_Of_Enrollment']
       blood_group=resultData['blood_group']
       marital_status=resultData['marital_status']
       wedding_aniversary_date=resultData['wedding_aniversary_date']
       house_hold_status=resultData['house_hold_status']
       income_level=resultData['income_level']
       height=float(resultData['height'])
       weight=float(resultData['weight'])
       occupation=resultData['occupation']
       community=resultData['community']
       religion=resultData['religion']
       family_relationship = json.loads(resultData['family_relationship'])


       try:
           add_member2=Add_Member2(
               title=title,
               first_name=first_name,
               middle_name=middle_name,
               last_name=last_name,
               gender=gender,
               email_id=email_id,
               age=age,dob=dob,
               mob_no=mob_no,
               address=address,
               pin_code=pin_code,
               date_Of_Enrollment=date_Of_Enrollment,
               blood_group= blood_group,
               marital_status=marital_status,
               wedding_aniversary_date= wedding_aniversary_date,
               house_hold_status=house_hold_status,
               income_level=income_level,
               height=height,
               weight=weight,
               occupation=occupation,
               community=community,
               religion=religion,
               family_relationship=family_relationship)
       except Exception as e:
           print("Errorsdsdsdsdsdsdsdsddsds is",e)


       add_member2.save()
       print("member created--------------")
       return redirect("/")
    else:
     return render(request,'add-member.html')

     
def view_edit_member(request):
     view_member = Add_Member2.objects.filter().values("id","title","first_name","dob","email_id")
     print("Myoutput1", view_member )
     context={ 
             'pop':view_member, 
             
            
              }
     return render(request,'view-edit-member.html',context)  
def view_member(request,id):
    obj=Add_Member2.objects.get(id=id)
    view_member1 = Add_Member2.objects.filter(id=obj.id).values("title","first_name","middle_name","last_name","gender","email_id","dob","age","mob_no","address","pin_code","date_Of_Enrollment","blood_group","marital_status",
                   "wedding_aniversary_date","house_hold_status","income_level","height","weight","occupation","community","religion","family_relationship")
    #import ipdb;ipdb.set_trace()
    try:
        import ast
        family_relationship =  ast.literal_eval( view_member1[0]['family_relationship'])
        #valid_json_string =  "[{0}]".format(family_relationship)
        #family_relationship = json.loads(valid_json_string)
    except Exception as e:
        print("Error in coinverstin string tod ict",family_relationship)
    context={  "viewMemb":view_member1,
                  "object":obj,
                  "family_relationship":family_relationship
                }

    print("asdasdsadsad",context["family_relationship"])
    return render(request,'view-member-detail.html', context) 

def edit_member(request,id):  
     member_ed = Add_Member2.objects.get(id=id)
     return render(request,'edit-member.html',{'mem':member_ed}) 

def member_update(request,id):
    updated_id=Add_Member2.objects.get(id=id)
    if request.method == "POST":
       print(request.POST)
       #import ipdb;ipdb.set_trace()
       resultData = prepareModelData(request.POST)

       print("inside if --------------")
       title=resultData['title']
       print("request.POST-----------------")
       first_name=resultData['first_name']
       print("first_name----------------")
       middle_name=resultData['middle_name']
       last_name=resultData['last_name']
       gender=resultData['gender']
       email_id=resultData['email_id']
       dob=resultData['dob']
       age=resultData['age']
       mob_no=resultData['mob_no']
       address=resultData['address']
       print("Address-----------------------######")
       pin_code=resultData['pin_code']
       date_Of_Enrollment=resultData['date_Of_Enrollment']
       blood_group=resultData['blood_group']
       marital_status=resultData['marital_status']
       wedding_aniversary_date=resultData['wedding_aniversary_date']
       house_hold_status=resultData['house_hold_status']
       income_level=resultData['income_level']
       height=float(resultData['height'])
       weight=float(resultData['weight'])
       occupation=resultData['occupation']
       community=resultData['community']
       religion=resultData['religion']
       family_relationship = json.loads(resultData['family_relationship'])


       try:
           update_member2=Add_Member2(
               title=title,
               first_name=first_name,
               middle_name=middle_name,
               last_name=last_name,
               gender=gender,
               email_id=email_id,
               age=age,dob=dob,
               mob_no=mob_no,
               address=address,
               pin_code=pin_code,
               date_Of_Enrollment=date_Of_Enrollment,
               blood_group= blood_group,
               marital_status=marital_status,
               wedding_aniversary_date= wedding_aniversary_date,
               house_hold_status=house_hold_status,
               income_level=income_level,
               height=height,
               weight=weight,
               occupation=occupation,
               community=community,
               religion=religion,
               family_relationship=family_relationship)
       except Exception as e:
           print("exception----------- is",e)


       member_update1=Add_Member2.objects.filter(id=updated_id.id).update(title=title,first_name=first_name,middle_name=middle_name,last_name=last_name,gender=gender,email_id=email_id,dob=dob,age=age,mob_no=mob_no,address=address,pin_code=pin_code,date_Of_Enrollment=date_Of_Enrollment,blood_group=blood_group,marital_status=marital_status,
                   wedding_aniversary_date=wedding_aniversary_date,house_hold_status=house_hold_status,income_level=income_level,height=height,weight=weight,occupation=occupation,community=community,religion=religion,family_relationship=family_relationship)
       context={  "mem":member_update1,          
                   "object":updated_id,
                }
       print("member updated--------------")
       return redirect("/")
    else:
        return render(request,'edit-member.html')



def prepareModelData(request):
    resultData = dict.fromkeys([f.get_attname() for f in Add_Member2._meta.fields])
    mapKey = {'Pincode':'pin_code','Income':'income_level','Email Id':'email_id','Mobile No':'mob_no','date':'date_Of_Enrollment','bg':'blood_group','Marital Status':'marital_status','wan':'wedding_aniversary_date','Household Status':'house_hold_status','ocpn':'occupation','commnty':'community','relgn':'religion'}
    familyRelationShipMap = {'full_name-1':'','relationship-1':'','mobile-no-1':'','email-id-1':'','pincode-1':'','date-picker-1':'','blood-group-1':'','gender-1':'',
                             'full_name-2':'','relationship-2':'','mobile-no-2':'','email-id-2':'','pincode-2':'','date-picker-2':'','blood-group-2':'','gender-2':'',
                             'full_name-3':'','relationship-3':'','mobile-no-3':'','email-id-3':'','pincode-3':'','date-picker-3':'','blood-group-3':'','gender-3':''}

    for key, value in request.items():
        print(key, value)
        if key in resultData:
            resultData[key] = value
        elif key.lower() in resultData:
            resultData[key.lower()] = value
        elif key in mapKey:
                resultData[mapKey[key]] = value
        elif key in familyRelationShipMap:
            familyRelationShipMap[key] = value
    resultData['family_relationship'] = json.dumps(familyRelationShipMap)
    resultData['id'] = getId()
    resultData['dob']  = getFormattedDate(resultData['dob'])
    try:
        resultData['date_Of_Enrollment'] = getFormattedDate(resultData['date_Of_Enrollment'])
    except:
        pass
    resultData['wedding_aniversary_date'] = getFormattedDate(resultData['wedding_aniversary_date'])

    return resultData


def getId():
    return "umr00000" + str(Add_Member2.objects.count())

def getFormattedDate(date):
    if(date):
        try:
            datetime.strftime(date, "%Y-%m-%d")
            return date
        except:
            date = datetime.strptime(date, "%m/%d/%Y")
            return (datetime.strftime(date, "%Y-%m-%d"))
    else:
        return None



