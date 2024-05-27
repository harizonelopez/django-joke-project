from django.shortcuts import render
from .models import Joke
import pyjokes

def home(request):
    category = request.GET.get('category', 'neutral')
    
    db_jokes = Joke.objects.all()

    pyjokes_list = [pyjokes.get_joke(category=category) for _ in range(5)]

    jokes = list(db_jokes)
    for joke in pyjokes_list:
        jokes.append(Joke(content=joke, author="PyJokes"))

    return render(request, 'jokes.html', {'jokes': jokes})

