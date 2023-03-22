from django.shortcuts import render

def inventario (request):
    context={"titulo":"inventario","inv":["clips","sacapuntas","marcadores","cartulina"]}
    return render(request,"inventario.html",context)