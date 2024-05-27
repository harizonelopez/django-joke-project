from django.shortcuts import render
from .models import Joke
import pyjokes

def joke_list(request):
    category = request.GET.get('category', 'neutral')
    
    # Fetch jokes from the database
    db_jokes = Joke.objects.all()

    # Fetch multiple jokes from pyjokes
    pyjokes_list = [pyjokes.get_joke(category=category) for _ in range(5)]

    # Combine database jokes and pyjokes
    jokes = list(db_jokes)
    for joke in pyjokes_list:
        jokes.append(Joke(content=joke, author="PyJokes"))

    return render(request, 'jokes.html', {'jokes': jokes})

