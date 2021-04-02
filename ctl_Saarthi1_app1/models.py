from django.db import models
from datetime import datetime
class Add_Member1(models.Model):
    PaymentG=(
   ('Cash','Cash'),
   ('CreditCard','CreditCard'),
   ('DebitCard','DebitCard'),
   ('Cheque','Cheque'),
   ('Paytm','Paytm'),
   ('Neft','Neft'),
          )


    title=models.CharField(max_length=120)
    first_name=models.CharField(max_length=120)
    middle_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    age=models.CharField(max_length=120)
    dob=models.DateField()
    mob_no=models.CharField(max_length=120)
    address=models.CharField(max_length=120)
    pin_code=models.CharField(max_length=120)
    comment=models.CharField(max_length=120)
    email_id=models.EmailField()
    test=models.CharField(max_length=120)
    total_amount=models.CharField(max_length=120)
    overall_discount=models.CharField(max_length=120)
    gross_amount=models.CharField(max_length=120)
    discount_amount=models.CharField(max_length=120)
    net_amount=models.CharField(max_length=120)
    due_amount=models.CharField(max_length=120)
    cash_amount=models.CharField(max_length=120)
    paid_amount=models.CharField(max_length=120)
    payment_getway=models.CharField(choices=PaymentG,max_length=128)
    remark=models.CharField(max_length=120)


class Add_Member2(models.Model):

    Title=(
        ('Mr' , 'Mr'),
		('Mrs' , 'Mrs'),
		('Miss','Miss'),
		('Baby of' , 'Baby of'),
		('Baba of', 'Baba of'),
		('Dr Mr' ,'Dr Mr'),
		('Dr Mrs' , 'Dr Mrs'),
		('Dr Miss' , 'Dr Miss'),
          )

    Gender=(
        ('Male' , 'Male'),
		('Female' , 'Female'),
		)

    Blood_Group=(
        ('A +ve' , 'A +ve'),
		('A -ve' , 'A -ve'),
        ('B +ve' , 'B +ve'),
		('B -ve' , 'B -ve'),
        ('O +ve' , 'O +ve'),
		('O -ve' , 'O -ve'),

		)


    Maritarial_Status=(
        ('Married' , 'Married'),
		('UnMarried' , 'UnMarried'),
        )

    HouseHold_Status=(
        ('Nuclear' , 'Nuclear'),
		('Joint' , 'Joint'),
        )
    Income_Level=(
        ('Lower' , 'Lower'),
		('Middle' , 'Middle'),
        ('Upper' , 'Upper'),
        ('HNI' , 'HNI'),
        )
    Occupation=(
        ('Worker' , 'Worker'),
		('Student' , 'Student'),
        ('Farming' , 'Farming'),
        ('Sales Job' , 'Sales Job'),
        ('HouseWife' , 'HouseWife'),
        ('Businessman' , 'Businessman'),
        ('Professional Job' , 'Professional Job'),
        ('Mangerial Job' , 'Mangerial Job'),
        ('Office Desk' , 'Office Desk'),
        ('Key Management' , 'Key Management'),
        )

    Community=(
        ('CTL Employee' , 'CTL Employee'),
		('CTL Family' , 'CTL Family'),
        ('CTL Vendor' , 'CTL Vendor'),
        ('GSB' , 'GSB'),
        ('Airoli Society' , 'Airoli Society'),
        )

    Religion=(
        ('Hindu','Hindu'),
		('Muslim','Muslim'),
        ('Christian','Christian'),
        ('Parsi','Parsi'),
        ('Buddhist','Buddhist'),
        ('Jain','Jain' ),
        ('Other','Other')
        )

    id = models.AutoField(primary_key=True, editable=False)
    reg_no = models.CharField(max_length=100, editable=False)
    title=models.CharField(choices=Title,max_length=128)
    first_name=models.CharField(max_length=120)
    middle_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    gender=models.CharField(choices=Gender,max_length=128)
    email_id=models.EmailField()
    dob=models.DateField()
    age=models.CharField(max_length=120)
    mob_no=models.CharField(max_length=120)
    address=models.CharField(max_length=120)
    pin_code=models.CharField(max_length=120)
    date_Of_Enrollment=models.DateField()
    blood_group=models.CharField(choices=Blood_Group,max_length=128)
    marital_status=models.CharField(choices=Maritarial_Status,max_length=128)
    wedding_aniversary_date=models.DateField(default=datetime.now, blank=True)
    house_hold_status=models.CharField(choices=HouseHold_Status,max_length=128)
    income_level=models.CharField(choices=Income_Level,max_length=128)
    height=models.FloatField()
    weight=models.FloatField() 
    occupation=models.CharField(choices=Occupation,max_length=128)
    community=models.CharField(choices=Community,max_length=128)
    religion=models.CharField(choices=Religion,max_length=128)
    family_relationship=models.TextField(blank=True, null=True)


    @property
    def familyrelationship(self):
        return dict(self.family_relationship)

    def save(self, **kwargs):
        if not self.reg_no:
            self.reg_no = "umr00000" + str(Add_Member2.objects.count())
        super().save(*kwargs)

