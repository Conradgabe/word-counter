from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    
def counter(request):
    text = request.POST['text']
    words_length = len(text.split())
    context = {'words_length': words_length}
    return render(request, 'counter.html', context)