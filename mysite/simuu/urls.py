from django.urls import path #,include
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'simuu'
urlpatterns = [
	path('', views.ListarSimulados.as_view(), name='listarSimulados'),
	path('listar_questoes/', views.ListarQuestoes.as_view(), name='listarQuestoes'),
	path('responder_simulado/<int:id_simulado>', views.ResponderSimulado.as_view(), name='responderSimulado'),
	path('submeter_simulado/', views.SubmeterFormulario.as_view(), name='submeterSimulado'),
	path('cadastro/', views.Cadastro.as_view(), name='cadastro'),
    path('login/',views.LoginUsuario.as_view(),name='login'),
    path('logout/',login_required(views.LogoutUsuario.as_view()),name='logout')
]
