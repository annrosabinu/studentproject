from django.urls import path
from .import views 

urlpatterns = [
    path('',views.studentreg,name='studentreg'),
    path('studentdetails',views.studentdetails,name='studentdetails'),
    path('showstudentdetails',views.showstudentdetails,name='showstudentdetails'),
    path('editdetails/<int:id>',views.editdetails,name='editdetails'),
    path('editpage/<int:id>',views.editpage,name='editpage'),
    path('deletepage/<int:id>',views.deletepage,name='deletepage'),
    path('viewpage/<int:id>',views.viewpage,name='viewpage'),
]