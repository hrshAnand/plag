from django.conf.urls import url
from plagapp import views
# SET THE NAMESPACE!
app_name = 'plagapp'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
	url(r'^index/$',views.register,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]