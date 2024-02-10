from django.shortcuts import render
from .forms import FileUploadForm, WordCountForm
from .word_counter import WordCounter

word_counter = WordCounter()


def home(request):
    file_form = FileUploadForm()
    word_form = WordCountForm()
    context = {'file_form': file_form, 'word_form': word_form}
    return render(request, 'home.html', context)


def load_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            content = file.read().decode('utf-8')
            word_counter.load_words_from_content(content)
    return render(request, 'home.html', {'file_form': FileUploadForm(), 'word_form': WordCountForm()})


def word_count(request):
    if request.method == 'POST':
        form = WordCountForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            count = word_counter.word_count(word)
            return render(request, 'home.html', {'file_form': FileUploadForm(), 'word_form': WordCountForm(), 'count': count})
    return render(request, 'home.html', {'file_form': FileUploadForm(), 'word_form': WordCountForm()})


def clear_memory(request):
    word_counter.clear_memory()
    return render(request, 'home.html', {'file_form': FileUploadForm(), 'word_form': WordCountForm()})
