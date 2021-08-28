from django.shortcuts import render
from random import randint
from datetime import datetime

# Create your views here.
def inicio(request):
    if "monto_oro" not in request.session:
        request.session['monto_oro'] = 0
        request.session['moves'] = []
    return render(request, 'index.html')

def process_money(request):
    time = datetime.now().strftime("%Y-%m-%d %H:%M %p")
    
    if "farm" in request.POST: # Si el POST viene de farm
        farmPrize = randint(10,20) # Valor aleatorio entre 10 y 20
        request.session['monto_oro'] += farmPrize # Se suma el valor aleatorio al valor de sesión
        request.session['moves'].append([farmPrize, 'farm', time]) #Se suma el valor a la variable de la sesion
        
    if "cave" in request.POST: # Si en el POST viene "cave"...
        cavePrize = randint(5,10) # Valor aleatorio entre 5 y 10
        request.session['monto_oro'] += cavePrize # Se suma el valor aleatorio al valor de sesión
        request.session['moves'].append([cavePrize, 'cave', time])
        
    if "house" in request.POST: # Si en el POST viene "house"...
        housePrize = randint(2,5) # Valor aleatorio entre 2 y 5
        request.session['monto_oro'] += housePrize # Se suma el valor aleatorio al valor de sesión
        request.session['moves'].append([housePrize, 'house', time])
        
    if "casino" in request.POST: # Si en el POST viene "casino"...
        casinoPrize = randint(-50, 50) # Valor aleatorio entre -50 y 50
        request.session['monto_oro'] += casinoPrize # Se suma o resta el valor aleatorio al valor de sesión
        request.session['moves'].append([casinoPrize, 'casino', time])
        
    return render(request, 'index.html')
