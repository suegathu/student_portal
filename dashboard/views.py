from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NotesForm, HomeworkForm, DashboardForm, TodoForm, ConversionForm, ConversionLengthForm, ConversionMassForm, UserRegistrationForm
from .models import Notes, Homework, Todo
from django.views import generic
from youtubesearchpython import VideosSearch
import requests
import wikipedia

def home(request):
    return render(request, 'dashboard/home.html')

def notes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user, title=request.POST['title'], description=request.POST['description'])
            notes.save()
            messages.success(request, f'Notes added from {request.user.username} successfully')
            return redirect('notes') 
    else:
        form = NotesForm()

    notes = Notes.objects.filter(user=request.user)  
    context = {
        'notes': notes,
        'form': form,
    }

    return render(request, 'dashboard/notes.html', context)

def delete_note(request, pk=NotImplemented):
    Notes.objects.get(id=pk).delete()
    return redirect('notes')

class NotesDetailView(generic.DetailView):
    model = Notes
    
def homework(request):
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            homeworks = Homework(
                user = request.user,
                subject = request.POST['subject'],
                title = request.POST['title'],
                description = request.POST['description'],
                due = request.POST['due'],
                is_finished = finished
            )        
            homeworks.save()
            messages.success(request, f'Homework added for {request.user.username}!') 
    else:       
        form = HomeworkForm()
    homeworks = Homework.objects.filter(user = request.user)
    if len(homeworks) == 0:
        homework_done = True
    else:
        homework_done = False    
    context = {
        'homeworks': homeworks,
        "homeworks_done": homework_done,
        'form': form
    }
    return render(request, 'dashboard/homework.html', context)
def update_homework(request, pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homework')       

def delete_homework(request, pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect('homework')     


def youtube(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            video = VideosSearch(text, limit=10)
            result_list = []
            for i in video.result()['result']:
                result_dict = {
                    'input': text,
                    'title': i['title'],
                    'duration': i['duration'],
                    'thumbnails': i['thumbnails'][0]['url'],
                    'channel': i['channel']['name'],
                    'link': i['link'],
                    'viewCount': i['viewCount']['short'],
                    'publishedTime': i['publishedTime'],
                }
                desc = ''
                if i['descriptionSnippet']:
                    for j in i['descriptionSnippet']:
                        desc += j['text']
                result_dict['description'] = desc
                result_list.append(result_dict)
            context = {
                'form': form,
                'results': result_list
            }
            return render(request, "dashboard/youtube.html", context)
    else:
        form = DashboardForm()
    
    context = {
        "form": form
    }
    return render(request, 'dashboard/youtube.html', context)

def todo(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False    
            except:
                finished = False
            todos = Todo(
                user = request.user,
                title = request.POST['title'],
                is_finished = finished
            ) 
            todos.save()
            messages.success(request, f'Todo added from {request.user.username}!')  
            return redirect('todo') 
        else:     
            form = TodoForm()  # FIXED: Instantiated the form properly

    todo = Todo.objects.filter(user=request.user)
    if len(todo) == 0:
        todos_done = True
    else:
        todos_done = False    

    context = {
        'form': form,
        'todos': todo,
        'todos_done': todos_done
    }
    return render(request, 'dashboard/todo.html', context)

def update_todo(request, pk=None):
    todo = Todo.objects.get(id=pk)
    if todo.is_finished == True:
        todo.is_finished = False
    else:
        todo.is_finished = True   
    todo.save()
    return redirect('todo')     
def delete_todo(request, pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect('todo')

def books(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            url = f'https://www.googleapis.com/books/v1/volumes?q={text}'
            r = requests.get(url)
            answer = r.json()
            result_list = []

            if 'items' in answer:  # Ensure the API returns results
                for i in range(min(10, len(answer['items']))):  # Avoid index error
                    volume_info = answer['items'][i]['volumeInfo']
                    result_dict = {
                        'title': volume_info.get('title', 'No title'),
                        'subtitle': volume_info.get('subtitle', 'No subtitle'),
                        'description': volume_info.get('description', 'No description'),
                        'count': volume_info.get('pageCount', 'N/A'),
                        'categories': volume_info.get('categories', ['No category']),
                        'rating': volume_info.get('averageRating', 'No rating'),
                        'thumbnail': volume_info.get('imageLinks', {}).get('thumbnail', ''),
                        'preview': volume_info.get('previewLink', '#'),
                    }
                    result_list.append(result_dict)

            context = {
                'form': form,
                'results': result_list
            }
            return render(request, "dashboard/books.html", context)
    else:
        form = DashboardForm()

    context = {
        "form": form
    }
    return render(request, 'dashboard/books.html', context)

def dictionary(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            url = f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{text}'
            r = requests.get(url)
            answer = r.json()

            if isinstance(answer, list) and len(answer) > 0:  # Ensure valid response
                word_data = answer[0]

                # ✅ Find the first available phonetic text & audio
                phonetics_text = 'N/A'
                audio_url = ''
                for phonetic in word_data.get('phonetics', []):
                    if phonetic.get('text'):
                        phonetics_text = phonetic['text']
                    if phonetic.get('audio'):
                        audio_url = phonetic['audio']
                        break  # Stop at the first available audio

                meanings = word_data.get('meanings', [{}])
                definitions = meanings[0].get('definitions', [{}])

                definition = definitions[0].get('definition', 'Definition not available')
                example = definitions[0].get('example', 'No example available')
                synonyms = definitions[0].get('synonyms', [])

                context = {
                    'form': form,
                    "input": text,
                    'phonetics': phonetics_text,
                    'audio': audio_url,
                    'definition': definition,
                    'example': example,
                    'synonyms': synonyms
                }
            else:
                context = {
                    'form': form,
                    'error': f"No definition found for '{text}'"
                }
            return render(request, 'dashboard/dictionary.html', context)
    
    else:
        form = DashboardForm()

    return render(request, 'dashboard/dictionary.html', {'form': form})

def wiki(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            form = DashboardForm(request.POST)
            search = wikipedia.page(text)
            context = {
                'form':form,
                'title': search.title,
                'link': search.url,
                'details': search.summary
            }
            return render(request, 'dashboard/wiki.html', context)
    else:
        form = DashboardForm()
        context = {
        'form': form
    }        
    return render(request, 'dashboard/wiki.html', context)

def conversion(request):
    if request.method == "POST":
        form = ConversionForm(request.POST)
        context = {'form': form, 'input': False}

        measurement = request.POST.get('measurement', '')

        if measurement == 'length':
            measurement_form = ConversionLengthForm()
            context.update({
                'm_form': measurement_form,
                'input': True
            })

            if 'input' in request.POST:
                first = request.POST.get['measure1']
                second = request.POST.get['measure2']
                input = request.POST.get['input']
                answer = ''

                if input and int(input) >= 0:
                    if first == 'yard' and second == 'foot':
                        answer = f'{input} yard = {int(input) * 3} foot'
                    elif first == 'foot' and second == 'yard':
                        answer = f'{input} foot = {int(input) / 3} yard'

                    context.update({'answer': answer})

        elif measurement == 'mass':
            measurement_form = ConversionMassForm()
            context.update({
                'm_form': measurement_form,
                'input': True
            })

            if 'input' in request.POST:
                first = request.POST.get['measure1']
                second = request.POST.get['measure2']
                input = request.POST.get['input']
                answer = ''

                if input and int(input) >= 0:
                    if first == 'pound' and second == 'kilogram':
                        answer = f'{input} pound = {int(input) * 0.453592} kilogram'
                    elif first == 'kilogram' and second == 'pound':  
                        answer = f'{input} kilogram = {int(input) * 2.20462} pounds'

                    context.update({
                        'answer': answer,
                        'form': form,
                        'm_form': measurement_form,
                        'input': True
                        })

    else:
        form = ConversionForm()
        context = {'form': form, 'input': False}

    return render(request, 'dashboard/conversion.html', context)

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} successfully')
            return redirect('login')  
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'dashboard/register.html', context)

def profile(request):
    return render(request, 'dashboard/profile.html')