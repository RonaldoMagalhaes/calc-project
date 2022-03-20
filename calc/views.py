from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def resposta(request):
    n1 = int(request.GET['n1'])
    n2 = int(request.GET['n2'])

    soma = n1 + n2
    sub = n1 - n2
    mult = n1 * n2
    if n2 != 0:
        div = n1/n2
    else:
        div = "Erro - divisao por zero"

    context = {"soma": soma, "sub": sub, "n1": n1, "n2": n2, "mult": mult, "div": div}

    print(n1)
    print(n2)

    return render(request, 'resposta.html', context)
