from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm, ProdutoModelForm

def home(request):
    return render(request, 'home.html')

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
            prod = form.save(commit=False)

            print(f'Nome: {prod.nome}')
            print(f'Preço: {prod.preco}')
            print(f'Estoque: {prod.estoque}')
            print(f'Imagem: {prod.imagem}')

            messages.success(request, 'Produto salvo com sucesso!')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao salvar produto!')
    else:
        form = ProdutoModelForm()
    
    context = { 'form': form }
    return render(request, 'produto.html', context)


