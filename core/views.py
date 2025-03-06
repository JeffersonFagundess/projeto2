from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

def home(request):
    context = {
        'produtos': Produto.objects.all()
    }  
    return render(request, 'home.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.send_email()
        messages.success(request, 'E-mail enviado com sucesso!')
        form = ContatoForm()
    elif form.errors:
        messages.error(request, 'Erro ao enviar e-mail!')
    
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto salvo com sucesso!')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao salvar produto!')
    else:
        form = ProdutoModelForm()
    
    context = { 'form': form }
    return render(request, 'produto.html', context)


