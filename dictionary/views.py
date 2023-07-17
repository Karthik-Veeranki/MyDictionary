from django.shortcuts import render

# Importing library necessary to find the meaning of a word
from PyDictionary import PyDictionary

# Importing library necessary to find the synonyms and antonymns of the word
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet



# Create your views here.

def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)

    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(search):
        for i in syn.lemmas():
            synonyms.append(i.name())
            if i.antonyms():
                antonyms.append(i.antonyms()[0].name())
    
    context = {
        'entered_word' : search,
        'meaning': meaning['Noun'][0],
        'synonyms': synonyms,
        'antonyms': antonyms
    }
    
    return render(request, 'word.html', context)