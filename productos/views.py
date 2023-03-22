from django.shortcuts import render

def productos(request):
    contex={"titulo":"productos","produ":["lapiz","cuaderno","borrador","calculadora"]}
    return render(request,"productos.html",contex)