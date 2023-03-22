from django.shortcuts import render

def clientes(request):
    client=["cliente_uno","cliente_dos","cliente_tres","cliente_cuatro"]
    context={"listado":client}
    return render(request, "clientes.html", context)

def listado_cli(request):
    context={}
    return render(request, "list_clientes.html", context)