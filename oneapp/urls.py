from oneapp import views
from django.urls import path

urlpatterns = [
    path('base/',views.base,name='base'),
    path('',views.log_in,name='login'),
    path('registration/',views.registration,name='registration'),
    path('registration/verifyotp/',views.verifyotp,name='verifyotp'),
    path('registration/verifyotp/password/',views.password,name='password'),
    path('registration/verifyotp/password/Error/',views.userRegister,name='userRegister'),
    path('logout/',views.log_out,name='logout'),
    path('myaccount/',views.profile,name='profile'),
    path('myaccount/aws/',views.aws,name='aws'),
    path('myaccount/vpc/',views.vpc,name='vpc'),
    path('myaccount/ec2/',views.ec2,name='ec2'),
    path('myaccount/s3/',views.s3,name='s3'),
    path('myaccount/report/',views.report,name='report')
]