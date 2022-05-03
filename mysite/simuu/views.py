from django.shortcuts import render,redirect
from simuu.models import Simulado,Questao,Resposta
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

# Create your views here.
class ListarSimulados(generic.ListView):
    model = Simulado
    context_object_name = 'simulados'
    template_name = 'simuu/listarSimulados.html'

class ListarQuestoes(generic.ListView):
    model = Questao
    context_object_name = 'questoes'
    template_name = 'simuu/listarQuestoes.html'

class ResponderSimulado(generic.View):
    def get(self, request, *args, **kwargs):
        try:
            simulado = Simulado.objects.get(pk=kwargs['id_simulado'])
        except (KeyError,Simulado.DoesNotExist):
            return redirect('simuu:listarSimulados')
        else:
            questoes = Questao.objects.filter(simulado=simulado)
            context = {'questoes': questoes,'simulado': simulado}
            return render(request,'simuu/responderSimulado.html',context)

class SubmeterFormulario(generic.View):
    def post(self, request, *args, **kwargs):
        try:
            id_simulado = request.POST["id_simulado"]
            simulado = Simulado.objects.get(pk=id_simulado)
        except (KeyError,Simulado.DoesNotExist):
            return redirect('simuu:listarSimulados')
        else:
            pontuacao_total = 0
            pontuacao_usuario = 0
            questoes = Questao.objects.filter(simulado=simulado)

            gabarito = {}

            for questao in questoes:
                resposta_correta = Resposta.objects.get(questao=questao,correta=True)
                resposta_usu = int(request.POST[('questao-'+str(questao.id))])
                resposta = Resposta.objects.get(pk=resposta_usu)

                # Verificar respostas
                if resposta_correta.id == resposta_usu:
                    pontuacao_usuario += questao.pontuacao
                    gabarito[questao] = {True: resposta}
                else:
                    gabarito[questao] = {False: resposta}
                pontuacao_total += questao.pontuacao

            context = {
                'gabarito': gabarito,
                'pontuacao_total': pontuacao_total,
                'pontuacao_usuario': pontuacao_usuario
            }
            return render(request,'simuu/pontuacao.html',context)

    def get(self, request, *args, **kwargs):
        return redirect('simuu:listarSimulados')



class Cadastro(generic.View):
    def get(self, request):
        return render(request,'simuu/cadastro.html')

    def post(self, request):
        caract = 6

        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password != cpassword:
            messages.add_message(request, messages.ERROR, "As senhas não conferem!")
            return redirect('simuu:cadastro')
        elif len(password) < caract:
            messages.add_message(request, messages.ERROR, "A senha precisa ter no mínimo 6 caracteres!")
            return redirect('simuu:cadastro')
        else:
            if User.objects.filter(username = username).first():
                messages.error(request, "Já existe usuário com esse username")
                return redirect('simuu:cadastro')
            User.objects.create_user(username=username,email=email,password=password,first_name=first_name)
            user_logado = authenticate(username=username,password=password)
            login(request,user_logado)
            return redirect('simuu:listarSimulados')



class LoginUsuario(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request,'simuu/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('simuu:listarSimulados')
        else:
            messages.add_message(request, messages.ERROR,"Usuário ou senha inválidos")
            return redirect('simuu:login')

class LogoutUsuario(generic.View):
    def get(self,request):
        logout(request)
        return redirect('simuu:login')


