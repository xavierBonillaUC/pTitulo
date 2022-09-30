from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('crearUsuario/', views.crearUsuario, name ='crearUsuario'),
    path('login/', views.login, name = 'login'),
    path('registrob/', views.registroB, name='registrob'),
    path('somos/', views.somos, name ='somos'),
    path('contacto/', views.contacto, name ='contacto'),
    path('editar/', views.editar, name ='editar'),
    path('eliminar/', views.eliminar, name ='eliminar'),
    path('loginAd/', views.loginAd, name ='loginAd'),
    path('pagAdmin/', views.pagAdmin, name ='pagAdmin'),
    path('pagFun/', views.pagFun, name ='pagFun'),
    path('crearUsuario/', views.crtUsuario, name ='crearUsuario'),
    path('crearUnInternas/', views.crtUnInternas, name ='crearUnInterna'),
    path('crearRoles/', views.crtRoles, name ='crearRoles'),
    path('crearFlujo/', views.crtFlujos, name ='crearFlujo'),
    path('crearTarea/', views.crtTarea, name ='crearTarea'),
    path('asignarResponsable/', views.asgResp, name ='asgResp'),
    
]