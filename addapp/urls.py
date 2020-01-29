from django.urls import path
from . import views
urlpatterns = [
  path('reg',views.reg,name='reg'),
  path('reglogic',views.reglogic,name='reglogic'),
  path('viewreg',views.viewreg,name='viewreg'),
  path('editreg',views.editreg,name='editreg'),
  path('deletereg',views.deletereg,name='deletereg'),
  path('deletecreg',views.deletecreg,name='deletecreg'),
  path('updatereg',views.updatereg,name='updatereg'),
  path('',views.index,name='index'),
  path('/addlogic',views.addlogic,name='addlogic')

]