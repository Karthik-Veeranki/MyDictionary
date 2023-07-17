# MyDictionary
This 'MyDictionary' project represents a user-friendly dictionary interface.

If a user wants to know the meaning of a word in English, they can enter the word and search for its meaning.

Once you press enter, you can see the word you have entered, the meaning of the word by default.

You have the option to view the synonyms and antonyms (if exists) for the same word.


Developed this application using **MVT** architecture of **Django** (Backend Python Web framework)

Integrated the **PyDictionary** library to find the meaning of the word and **nltk** library to find the synonyms and antonyms of the word.

Designed the frontend using **HTML**, **CSS**, **BootStrap5** and hosted the application on the localhost using Django's development server. 


Changes commited to the default framework are as follows:

In the dictionary folder,

--- To the default framework, added the urlpatterns in urls.py

--- Created the views for searching the meaning, synonyms, antonyms in views.py

In the englishdictionary folder,

--- Allowed all the hosts to deploy the application and added an entry regarding sqlite3 in the DATABASES section in settings.oy

--- Included path in urls.py

In the templates folder, 

--- The default template web page is 'index.html' that consists of frontend HTML and CSS BootStrap to decorate. Also takes input word from user.

--- The redirecting template 'word.html' integrates the django syntax to HTML and fetches the results from views.py and displays them on screen.

Finally to run the application on localhost, type the command in the parent folder:
--- py manage.py runserver
