from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

import random

def scramble_word(word):
    if len(word) > 3:
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]
    return word

def process_text(request):
    if request.method == 'POST' and request.FILES['text_file']:
        file = request.FILES['text_file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        with fs.open(filename) as f:
            content = f.read().decode('utf-8')
            words = content.split()
            scrambled_text = ' '.join(scramble_word(word) for word in words)
        return render(request, 'text_processor/text_result.html', {'text': scrambled_text})
    return render(request, 'text_processor/upload.html')