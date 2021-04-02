from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('',views.login,name='home'),
    path('login/',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('department',views.department,name='department'),
    path('membership',views.membership,name='membership'),
    path('add-member/',views.add_member,name='add-member'),
    path('view-edit-member',views.view_edit_member,name='view-edit-member'),
    path('view-member-detail/<int:id>/',views.view_member,name='view-member-detail'),
     path('view-member-detail-copy',views.demo,name='view-member-detail-copy'),
    path('view-member-detail/edit-member/<int:id>/',views.edit_member,name='edit-member'),
    path('member_update/<int:id>',views.member_update,name='edit-member'),
    
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

     path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
     name="password_reset_done"),

     path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
     
     name="password_reset_confirm"),

     path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
     name="password_reset_complete"),
]