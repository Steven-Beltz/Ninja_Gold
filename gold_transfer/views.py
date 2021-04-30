from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
#Presents options for player
    if 'count' not in request.session or 'activities' not in request.session:
        request.session['count'] = 0
        request.session['activities'] = []
    return render (request, 'index.html')

def money(request):
    if request.method == 'GET' :
        return redirect ('/')
# Method = Post, establish variables
    totalGold = request.session['count']
    location = request.POST['location']
    date = datetime.now().strftime('%m/%d/%Y %I:%M %p')
# Generate random number based on location name
    if location == 'farm':
        goldTurn = random.randint(10,20)
    elif location == 'cave':
        goldTurn = random.randint(5,10)
    elif location == 'house':
        goldTurn = random.randint(2,5)
    else:
        goldTurn = random.randint(0,50)
        winLose = random.randint(0,1)
        if winLose == 0:
            goldTurn *= -1
# Add the random number to total gold that is then put back into session. 
    totalGold += goldTurn
    request.session['count'] = totalGold
# Generate a message based on if the gold was positive or negative to the total
    if goldTurn >= 0:
        message = f"Entered {location} and earned {goldTurn} ({date})"
    else:
        goldTurn *= -1
        message = f"Entered {location} and lost {goldTurn} ({date})"
    request.session['activities'].append(message)
# Redirect back to the option page, with new information based on the turn
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')