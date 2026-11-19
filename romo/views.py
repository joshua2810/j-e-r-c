from django.shortcuts import render

def inicio  (request) :
    return render (request, "romo/inicio.html") 

def registro (request) :
    return render (request, "romo/formregistro.html")
